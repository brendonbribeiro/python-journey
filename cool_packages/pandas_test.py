#Work with data files and tables
import pandas

data_frame = pandas.read_json("files/supermarkets.json")
data_frame.set_index("ID")
print(data_frame)
