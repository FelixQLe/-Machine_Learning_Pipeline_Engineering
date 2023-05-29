from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from multiprocessing import cpu_count
from airflow.providers.postgres.operators.postgres import PostgresOperator
from utils.data_processing import data_processing
from utils.feature_engineering import feature_engineering
from utils.fetching_best_model import best_model_search
from utils.storing_metrics_to_database import track_experiments_info
from utils.create_connection import create_connection_task

default_args = {
    'owner': 'Felix Le',
    'email_on_failure': False,
    'email': ['lequanghop844@gmail.com'],
    'start_date': datetime(2021, 1, 1),
}

dag = DAG("ml_pipeline",
          description='End-to-end ML pipeline',
          schedule=None,
          default_args=default_args,
          catchup=False)


#get batch number for parallel processing
n_processor = cpu_count()

create_pg_connection_task = PythonOperator(
                                        task_id='create_pg_connection_task',
                                        python_callable=create_connection_task,
                                        dag=dag,
                                        )

creating_ml_metrics_table_task = PostgresOperator(
                                        task_id ="creating_ml_metrics_table_task",
                                        postgres_conn_id='pg_work_sample',
                                        sql='sql/create_tracking_best_model_table.sql',
                                        dag=dag
                                        )

machine_learning_task = PythonOperator(task_id='machine_learning_task',
                                       python_callable=best_model_search,
                                       dag=dag,
                                       )

collecting_all_metrics = PostgresOperator(task_id="collecting_all_metrics",
                                          postgres_conn_id='pg_work_sample',
                                          sql="SELECT * FROM tracking_best_model;",
                                          dag=dag
                                          )

storing_metrics_to_database_task = PythonOperator(task_id='storing_metrics_to_database_task',
                                                  python_callable=track_experiments_info,
                                                  dag=dag
                                                  )

processing_tasks = []
featuring_tasks = []
for n in range(n_processor):
    task_id = f'data_processing_task{n}'
    task = PythonOperator(task_id=task_id,
                          python_callable=data_processing,
                          op_kwargs={'batch_number': n},
                          dag=dag,
                        )
    processing_tasks.append(task)


for n in range(n_processor):
    task_id = f'featuring_data_task{n}'
    task = PythonOperator(task_id=task_id,
                          python_callable=feature_engineering,
                          op_kwargs={'batch_number': n},
                          dag=dag
                        )
    featuring_tasks.append(task)


for i in range(n_processor):
    create_pg_connection_task >> creating_ml_metrics_table_task >> processing_tasks[i] >> featuring_tasks[i] >> machine_learning_task >> storing_metrics_to_database_task >> collecting_all_metrics


