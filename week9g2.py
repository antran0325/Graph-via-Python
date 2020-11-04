#ANN TRAN 
import numpy as np
import matplotlib.pyplot as plt
import csv
from csv import reader
subject = []
count = []

with open('CountHeader.csv','r',encoding='utf8')as readFile:
    data = list(reader(readFile))
    for y in range (len(data)):
        subject.append(data[y][0])
        #print("Year: ",str(subject[y]), "\t")
        count.append(data[y][1])
        #print("count: ",str(count[y]), "\n")

#set up the figure
fig = plt.figure()
#create axes - one row, one column, one plot
ax = fig.add_subplot(111)

#set up marks for the y axis
y_pos = np.arange(len(subject))

#create the graph
ax.barh(y_pos, count, align='center', color='r', alpha=0.4)
#set labels and spacing for y axis
plt.yticks(y_pos, subject)
#label x axis
plt.xlabel('Subjects in programming books')
#label figure
plt.title("How many times each subject heading is mentioned ")

#show the figure
plt.show()
