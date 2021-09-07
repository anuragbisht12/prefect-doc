    """Functional API
    """
from prefect import task, Flow
from prefect.tasks.shell import ShellTask

# Will only return the listed files
ls_task = ShellTask(command="ls", return_all=True)

@task
def show_output(std_out):
    print(std_out)

with Flow("count_files") as flow:
    ls = ls_task()
    show_output(ls)

    # Override command to count listed files
    ls_count = ls_task(command="ls | wc -l")
    show_output(ls_count)

""" Imperative API"""
from prefect import Task, Flow
from prefect.tasks.shell import ShellTask

class ShowOutput(Task):
    def run(self, std_out):
        print(std_out)

ls_task = ShellTask(command="ls", return_all=True)
show_output = ShowOutput()

ls_count = ShellTask(command="ls | wc -l", return_all=True)
show_output2 = ShowOutput()

flow = Flow("count_files")
show_output.set_upstream(ls_task, key="std_out", flow=flow)
show_output2.set_upstream(ls_count, key="std_out", flow=flow)
