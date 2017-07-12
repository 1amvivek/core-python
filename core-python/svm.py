import numpy as np
import matplotlib.pyplot as plot
from sklearn import svm, datasets
import datetime
import psutil
import os



start = datetime.datetime.now()

iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target

print(type(y))
print(y)
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

end = datetime.datetime.now()

print("Processing Time ", end-start)
pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
print('CPU Utilization: ', memoryUse)
print('CPU Utilization percentage ', psutil.cpu_percent())
print('CPU virtual memory usage ', psutil.virtual_memory()) #  physical memory usage

plot.show()



