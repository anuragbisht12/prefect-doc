from prefect import task
from prefect.engine import TaskRunner


@task
def number_task():
    return 42

runner = TaskRunner(task=number_task)
state = runner.run()

assert state.is_successful()
assert state.result == 42
