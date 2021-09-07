from prefect import Flow

f = Flow("example")
f.add_task(number_task)

print(f.tasks) # {<Task: number_task>}


# another way
with Flow("example-v2") as f:
    result = number_task()

print(f.tasks) # {<Task: number_task>}
