from datetime import timedelta, datetime
from prefect.schedules import IntervalSchedule

# ... task definitions ...

schedule = IntervalSchedule(
    start_date=datetime.utcnow() + timedelta(seconds=1),
    interval=timedelta(minutes=1),
)

with Flow("Aircraft-ETL", schedule=schedule) as flow:
    airport = Parameter("airport", default="IAD")
    radius = Parameter("radius", default=200)

    reference_data = extract_reference_data()
    live_data = extract_live_data(airport, radius, reference_data)

    transformed_live_data = transform(live_data, reference_data)

    load_reference_data(reference_data)
    load_live_data(transformed_live_data)
