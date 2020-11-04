#ANN TRAN 
import numpy as np
import matplotlib.pyplot as plt
import csv
from csv import reader
doc = []
count = []
with open('CountType.csv','r',encoding='utf8')as readFile:
    data = list(reader(readFile))
    for y in range (len(data)):
        doc.append(data[y][0])
        print("doc: ",str(doc[y]), "\t")
        count.append(data[y][1])
        print("count: ",str(count[y]), "\n")

#set up the figure
fig = plt.figure()
#create axes - one row, one column, one plot
ax = fig.add_subplot(111)

#set up marks for the y axis
y_pos = np.arange(len(doc))

#create the graph
ax.barh(y_pos, count, align='center', color='r', alpha=0.4)
#set labels and spacing for y axis
plt.yticks(y_pos, doc)
#label x axis
plt.xlabel('Types of doc')
#label figure
plt.title("Which type doc do books belong to?")

#show the figure
plt.show()

