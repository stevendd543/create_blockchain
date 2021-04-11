import socket
import data_def

data_list = []
# create sender data
data = data_def.basic_data("Peter", "Andy", "1", "new year")
data.add_data_to_list()
data.send_data()
