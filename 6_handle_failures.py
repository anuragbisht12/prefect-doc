from datetime import timedelta
import aircraftlib as aclib
from prefect import task, Flow, Parameter


@task(max_retries=3, retry_delay=timedelta(seconds=10))
def extract_reference_data():
    # same as before ...
    pass


@task(max_retries=3, retry_delay=timedelta(seconds=10))
def extract_live_data(airport, radius, ref_data):
    # same as before ...
    pass

