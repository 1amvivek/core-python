import csv
import numpy as np
import matplotlib.pyplot as plot
from sklearn import svm
import datetime
import psutil
import os

start = datetime.datetime.now()

X = []
y = []

with open('input.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        tempX = []
        try:
            X0 = float(row[0])
            X1 = float(row[1])
            y0 = int(row[2])
        except ValueError as v:
            print("Ignored value", row)


        if isinstance(X0, float):
            tempX.append(X0)
        else:
            continue
        if isinstance(X1, float):
            tempX.append(X1)
        else:
            continue
        if isinstance(y0, int):
            X.append(tempX)
            y.append(y0)
        else:
            continue

X = np.array(X)
y = np.array(y)

h = .02

C = 1.0

svc = svm.SVC(kernel='linear', C=C).fit(X, y)

# X Co-ordinates

x_min = X[:, 0].min() - 1
x_max = X[:, 0].max() + 1

# Y Co-ordinates
y_min = X[:, 1].min() - 1
y_max = X[:, 1].max() + 1


xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))


Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plot.xlabel('IRIS Sepal length')
plot.ylabel('IRIS Sepal width')
plot.title('Support Vector Machine')
plot.contourf(xx, yy, Z, cmap=plot.cm.coolwarm, alpha=0.8)
plot.scatter(X[:, 0], X[:, 1], c=y, cmap=plot.cm.coolwarm)

plot.xlim(xx.min(), xx.max())
plot.ylim(yy.min(), yy.max())

plot.xticks(())
plot.yticks(())

array = []

for index in range(len(X)):
    temp = X[index].tolist()
    temp.append(y[index])
    array.append(temp)


csvFileObj = open('output.csv', 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in array:
    csvWriter.writerow(row)
csvFileObj.close()

end = datetime.datetime.now()

print("Processing Time: ", end-start)
pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30
print('CPU Utilization: ', memoryUse)
print('CPU Utilization percentage: ', psutil.cpu_percent())
print('CPU virtual memory usage: ', psutil.virtual_memory())

plot.show()