from sklearn import datasets, tree, linear_model
from IPython.display import Image
from sklearn.externals.six import StringIO
from sklearn.cross_validation import train_test_split
from matplotlib import pyplot as mp
import numpy as np
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import scipy
from sklearn import svm
import pydot
import matplotlib.pyplot as plt
import sys
from operator import add

from time import time
sys.path.append("../Assignment4/")

z =[]
test=[]
X = [[0, 0], [0, 2], [2,0], [2,1], [1,2], [2,3], [5,1], [3,2], [3,3], [4,2], [4,3], [4,4], [5,2], [1, 1]]
Y = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

for i in range(len(X)):
    z.append(map(add, X[i], [7,8]))
    test.append(map(add, X[i], [4,2]))
Y1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1, 1, 1]
y1=np.array(Y1)
X=np.array(X)
z=np.array(z)
test=np.array(test).tolist()
regr = linear_model.LinearRegression()



#model = linear_model.LinearRegression()
#model.fit(x_train,y_train)




xax = np.concatenate((X,z), axis = 0)
clf = svm.SVC()
clf=clf.fit(xax, y1)

#print clf.predict([[8,8]])

# Plot
plt.scatter(X[:,0], X[:,1], marker='+',color='blue')
plt.scatter(z[:,0], z[:,1],marker='o',color='red')

print clf.predict(test)
#plt.show()
#print y1
