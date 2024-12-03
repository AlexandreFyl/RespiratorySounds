# import os
# import json
# import requests
# from sqlalchemy.sql import text
# from sqlalchemy import create_engine
# import pandas as pd
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


def train():
    pass


def test():
    pass


# DAG configuration
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "traitement_son_dag",
    default_args=default_args,
    description="Pipeline pour le traitement des données sonores, entrainement du modèle et prédiction",
    schedule=timedelta(days=1),
    start_date=datetime(2024, 12, 2),
    catchup=False,
) as dag:

    # Task definition
    geolocation_task = PythonOperator(
        task_id="train",
        python_callable=train,
    )

    geolocation_task = PythonOperator(
        task_id="test",
        python_callable=test,
    )

    # Task dependencies and execution flow
    train >> test
