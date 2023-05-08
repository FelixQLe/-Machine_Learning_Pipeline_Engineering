# Base image
FROM apache/airflow:2.6.0

USER airflow
RUN pip install --no-cache-dir \
    tensorflow \
    scikit-learn \