#https://docs.greatexpectations.io/docs/core/introduction/try_gx
#Version for demo 1.0.0

#Prequisites: Python version 3.8 to 3.11

#pip3 install pandas
#pip3 install great_expectations


#1- Import the following libraries
import great_expectations as gx
# Pandas -> 
import pandas as pd

# -> Line to check gx core version: print(gx.__version__)

# 2- Download and read the sample data into a Pandas DataFrame.
df = pd.read_csv(
    "https://raw.githubusercontent.com/great-expectations/gx_tutorials/main/data/yellow_tripdata_sample_2019-01.csv"
)

#3- A Data Context object serves as the entrypoint for interacting with GX components.
context = gx.get_context()

#4- Connect to data and create a Batch.
# Define a Data Source, Data Asset, Batch Definition, and Batch. The Pandas DataFrame is provided to the Batch Definition at runtime to create the Batch.

data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})


#Create an Expectation.
#Expectations are a fundamental component of GX. They allow you to explicitly define the state to which your data should conform.
#Run the following code to define an Expectation that the contents of the column passenger_count consist of values ranging from 1 to 6:



expectation = gx.expectations.ExpectColumnValuesToBeBetween(
    column="passenger_count", min_value=2, max_value=6
)


#Run and get the results!
validation_result = batch.validate(expectation)

print(validation_result)