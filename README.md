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

### Airflow docker compose
- docker-compose.yaml
- Dockerfile, containing dependencies will be installed for first time run docker-compose up
### Directory structure: 
directory_structure.txt, showed in the end of this README.md


dags subrepo: 
- contain all python and sql scripts, ml_pipeline run on Apache Airflow, training_log, training_metrics, data

### Machine Learning architecture

- Task 1: create a new connection to postgres
- Task 2: create sql table to store machine learning best params
- Group task 1(task 3-10): waiting for task one completed successfully, use 8 processors to process 8 patchs of df
- Group task 2(task 11-18): waiting for group ask 1 completed sucessfully, use 8 processors to process 8 processed-batchs from group 1
- Task final: save ML best params, loss, scores to sql table created from task 1

![Screenshot 2023-05-29 at 2 45 13 AM](https://github.com/FelixQLe/Work_Sample_ML_Pipeline/assets/93171100/966e3e97-ac45-47fc-a6d8-01c357c993f8)

![Screenshot 2023-05-29 at 2 46 17 AM](https://github.com/FelixQLe/Work_Sample_ML_Pipeline/assets/93171100/a515dff4-6403-4e16-a160-bf1427af2982)

![Screenshot 2023-05-29 at 2 47 30 AM](https://github.com/FelixQLe/Work_Sample_ML_Pipeline/assets/93171100/c487375e-a82f-419b-9a28-91900142fe29)


### Model_API subrepo:
- contain flask API app, deploying ml_model to predict trading Volume, and how_to_run.txt
- result:
![Screenshot 2023-05-08 at 12 33 01 PM](https://user-images.githubusercontent.com/93171100/236879582-933e51cf-fbcf-4eca-afcb-3055db07d267.png)
![Screenshot 2023-05-08 at 12 54 44 PM](https://user-images.githubusercontent.com/93171100/236884019-1195fdd6-977c-48b7-8269-091ef485ab3e.png)

### Directory Airflow ML Pipeline Structure:
![Screenshot 2023-05-29 at 3 18 24 PM](https://github.com/FelixQLe/Work_Sample_ML_Pipeline/assets/93171100/644ad518-fae6-4be1-be87-dd4619bf0824)
![Screenshot 2023-05-29 at 3 18 41 PM](https://github.com/FelixQLe/Work_Sample_ML_Pipeline/assets/93171100/ec1187a0-3a3f-4b66-8937-260a5d0be5c6)
