from prefect import Flow
from prefect.tasks.shell import ShellTask
 
shell = ShellTask()
with Flow("Simple Pipeline") as flow:
   flow.chain(
       shell(command='pip install -r requirements.txt'),
       shell(command='black --check .'),
       shell(command='pytest .'),
   )
 
flow.run()
