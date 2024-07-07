from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime as dt

default_args = {
    'owner': 'Bavenraj',
    'start_date': dt.datetime(2024,8,10),
    'retries': 5,
    'retry_delay': dt.timedelta(minutes=1),
}

with DAG(
    dag_id = 'simple_example',
    description = 'A simple DAG',
    default_args = default_args,
    schedule_interval = "@daily", 
) as dag:
    task1 = BashOperator(
        task_id = 'print_hello',
        bash_command = 'echo \'Greetings. the date and time are \'',
    )
    task2 = BashOperator(
        task_id = 'print_date',
        bash_command = 'date',
    )
    task1 >> task2