from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': "baven",
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id = "sample_etl",
    default_args= default_args,
    description = "testing",
    start_date = datetime(2024, 5, 7),
    schedule_interval = timedelta(days=10)
) as dag:
    extract = BashOperator(
        task_id = "extract1",
        bash_command = 'echo "extract1"'
    )
    transform = BashOperator(
        task_id = 'transform1',
        bash_command = 'echo "transform1"'
    )
    load = BashOperator(
        task_id = 'load1',
        bash_command = 'echo "load1"'
    )
    extract >> transform >> load