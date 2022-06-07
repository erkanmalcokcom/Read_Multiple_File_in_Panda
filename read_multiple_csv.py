import pandas as pd
import time
start = time.time()
# File list into the array list
data_list = ["data-0{0}.tsv".format(i) for i in range(1, 8)]
data_name = []
for i in range(7):
  x = data_list[i].strip(".tsv")
  data_name.append(x)

for i in range(7):
  data_name[i] = pd.read_csv("/Users/erkanmalcok/VS Code/imdb/raw_data/{0}.tsv".format(data_name[i]), sep='\t', nrows=10000)

for i in range(7):
  print(data_name[i].head())

end = time.time()
print("")

print("____________________________________________________________")

print("Total time of the process:", end-start)

print("____________________________________________________________")
print("RESULT")
while end-start < 1:
  print("We have processed all files less than one minute.")
  break