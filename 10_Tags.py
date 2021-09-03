from prefect import tags

with tags('red', 'blue'):
    t = Task()

assert t.tags == {'red', 'blue'}



flow.get_tasks(name='my-task')
flow.get_tasks(tags=['red'])
