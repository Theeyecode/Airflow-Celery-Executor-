from airflow.sdk import dag, task , task_group


@dag
def group():

    @task
    def a():
        return 42
    
    @task_group(default_args={
        'retries':2
    })
    def my_group(val: int):
        @task
        def b(my_val: int):
            print(my_val + 8)      
        
        @task_group(default_args={
            'retries':3
        })

        def my_nested_group():
            @task
            def x():
                print("x")

            @task
            def y():
                print("y")
            x() >> y()
        @task
        def c():        
            print("c")
        b(val) >> my_nested_group() >> c()

    val = a() 
    my_group(val)

group()