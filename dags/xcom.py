from airflow.sdk import dag, task, Context


@dag
def xcom_dag():
    
    @task
    def t1(context: Context):
        val = 42
        context['t1'].xcom_push(key='my_key', val = val)

    @task
    def t2(context: Context):
        val = context['t1'].xcom_pull(key='my_key', task_ids='t1')
        print(val)

    t1() >> t2()

xcom_dag()