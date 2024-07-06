from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'bavenraj',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

@dag(dag_id='dag_taskflow_api', 
     default_args = default_args,
     start_date = datetime(2024, 6, 29), # run 2 am
     schedule_interval = '@daily')
def hello_world_etl():
    
    @task(multiple_outputs = True)
    def get_name():
        return {'first_name': 'Tom',
                'last_name': 'Jerry'}
    
    @task()
    def get_age():
        return 23
    
    @task()
    def greet(first_name, last_name, age):
        print(f"Hello {first_name} {last_name} " f"Is your age is {age}?")
        
    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'],last_name=name_dict['last_name'], age=age)
    
greet_dag = hello_world_etl()