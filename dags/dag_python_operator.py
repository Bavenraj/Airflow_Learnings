from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'bavenraj',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids = 'get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids = 'get_name', key='last_name')
    age = ti.xcom_pull(task_ids = 'get_age', key='age')
    print(f"hello how are you {first_name} {last_name}." f" is your age {age}?")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Tom')
    ti.xcom_push(key='last_name', value='Jerry')

def get_age(ti):
    ti.xcom_push(key='age', value=22)
    
with DAG(
    dag_id='DAG_python_operator_V1',
    default_args = default_args,
    description= 'Our first dag with python operator',
    start_date = datetime(2024, 6, 29, 2), # run 2 am
    schedule_interval = '@daily'
) as dag:
    
   task1 = PythonOperator(
       task_id="greet_function",
       python_callable = greet,
       op_kwargs = {'age': 23}
   )
   
   task2 = PythonOperator(
       task_id="get_name",
       python_callable = get_name,
   )
   
   task3 = PythonOperator(
       task_id = "get_age",
       python_callable = get_age,
   )
   
   [task2, task3] >> task1