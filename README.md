# Machine Learning Workflow
### Evaluations

- Problem 1: Raw Data Processing  
- Problem 2: Feature Engineering
- Problem 3: Integrate ML Training
- Problem 4: Model Serving
  https://github.com/FelixQLe/Deploying_MLModel_Automate_Loan_Eligibility_FLaskAPI
### References for designing Airflow workflow, problem 1-3
- https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html#testing
- https://towardsdatascience.com/end-to-end-machine-learning-pipeline-with-docker-and-apache-airflow-from-scratch-35f6a75f57ad
- https://github.com/btphan95/greenr-airflow
- https://betterdatascience.com/apache-airflow-run-tasks-in-parallel/
- https://stackoverflow.com/questions/52741536/running-airflow-tasks-dags-in-parallel
- https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas
- https://www.simplilearn.com/tutorials/python-tutorial/map-in-python
- https://stackoverflow.com/questions/50337843/extract-file-name-from-read-csv-python
- https://sparkbyexamples.com/pandas/pandas-read-multiple-csv-files/?amp=1

### Directory structure: 
directory_structure.txt

dags: 
- contain all python and sql scripts, ml_pipeline run on Apache Airflow, training_log, training_metrics, data

### Machine Learning architecture

- Task 1: create sql table to store machine learning best params
- Group task 1(task 2-9): waiting for task one completed successfully, use 8 processors to process 8 patchs of df
- Group task 2(task 10-17): waiting for group ask 1 completed sucessfully, use 8 processors to process 8 processed-batchs from group 1
- Task final: save ML best params, loss, scores to sql table created from task 1

![Screenshot 2023-05-08 at 4 15 13 AM](https://user-images.githubusercontent.com/93171100/236777778-297e7f10-01a0-467c-82d5-218d319f6836.png)

<img width="1367" alt="Screenshot 2023-05-08 at 4 40 41 AM" src="https://user-images.githubusercontent.com/93171100/236777950-0e9d9121-0f58-498b-8c38-c23a8733d49a.png">

### Model_API:
- contain flask API app, deploying ml_model to predict trading Volume, and ho_to_run.txt
- result:
![Screenshot 2023-05-08 at 12 33 01 PM](https://user-images.githubusercontent.com/93171100/236879582-933e51cf-fbcf-4eca-afcb-3055db07d267.png)
![Screenshot 2023-05-08 at 12 54 44 PM](https://user-images.githubusercontent.com/93171100/236884019-1195fdd6-977c-48b7-8269-091ef485ab3e.png)

