from airflow.sdk import dag, task 
from time import sleep


@dag
def clelery_dag():

    @task
    def a():
        sleep(5)

    @task
    def b():
        sleep(5)

    @task
    def c():
        sleep(5)

    @task
    def d():
        sleep(5)
#Define task dependencies
    a() >> [b(), c()] >> d()
    
clelery_dag()