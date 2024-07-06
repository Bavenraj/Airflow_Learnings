from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Bavenraj',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='DAG_catchup_backfill',
    default_args = default_args,
    description= 'Dag with catchup and backfill',
    start_date = datetime(2024, 5, 29), 
    schedule_interval = '@daily',
    catchup = True
) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command = "echo this is the simple bash command"
    )
     