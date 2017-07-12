from sklearn import datasets
import csv


iris = datasets.load_iris()

X = list(iris.data[:, :2])
y = list(iris.target)

array = []


for index in range(len(X)):
    temp = X[index].tolist()
    temp.append(y[index])
    array.append(temp)

print(array)

csvFileObj = open('output.csv', 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in array:
    csvWriter.writerow(row)
csvFileObj.close()





