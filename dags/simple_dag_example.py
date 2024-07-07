from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Bavenraj',
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id = 'simple_example',
    description = 'A simple DAG',
    default_args = default_args,
    start_date = datetime(2024, 6, 30, 2), # run 2 am
    schedule_interval = "@daily" 
) as dag:
    task1 = BashOperator(
        task_id = 'print_hello',
        bash_command = 'echo \'Greetings. the date and time are \''
    )
    task2 = BashOperator(
        task_id = 'print_date',
        bash_command = 'date'
    )
    task1 >> task2