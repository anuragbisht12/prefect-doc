from prefect.engine.results import LocalResult

result = LocalResult(dir="./my-results")

@task
def load_reference_data(ref_data):
    logger = prefect.context.get("logger")
    logger.info("saving reference data...")

    db = aclib.Database()
    db.update_reference_data(ref_data)



with Flow("Aircraft-ETL", result=result) as flow:
    ...

flow.run()
