import csv
import pandas
import pyarrow

data = pandas.read_csv("squirrel_data.csv")

new_data = pandas.DataFrame(data["Primary Fur Color"].value_counts())

new_data.to_csv("squirrel.csv")