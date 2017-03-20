import matplotlib.pyplot as plt
import csv
from time import gmtime, strftime

time = []
memory = []
user = []

with open('/Users/dbento/Downloads/psacct-201703111439.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        time.append(int(row[0]))
        memory.append(int(row[1]))
        user.append(str(row[2]))

#plt.pie(time, memory)
plt.plot(time, memory, label='Loaded from file')
plt.xlabel('Number of Users\nTime of snapshot')
plt.ylabel('Memory In KB')
plt.legend()
plt.title('Summay Graph\nView of User001')
plt.show()
