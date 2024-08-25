import great_expectations as gx

#Create a DataContext
context = gx.get_context()

#Connect to Data
validator = context.sources.pandas_default.read_csv(
    "https://raw.githubusercontent.com/great-expectations/gx_tutorials/main/data/yellow_tripdata_sample_2019-01.csv"
)

#Create Expectations
validator.expect_column_values_to_not_be_null("pickup_datetime")
validator.expect_column_values_to_be_between(
    column="passenger_count",
    min_value=0,  # Replace with your desired minimum value
    max_value=10,  # Replace with your desired maximum value
)
validator.expect_column_to_exist("fake_column")
validator.save_expectation_suite()

#Validate data
checkpoint = context.add_or_update_checkpoint(
    name="my_quickstart_checkpoint",
    validator=validator,
)

checkpoint_result = checkpoint.run()

context.view_validation_result(checkpoint_result)