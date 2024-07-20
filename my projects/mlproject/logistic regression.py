# to train the logistic regression to predict either the flower is verginica
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
iris=datasets.load_iris()
# 
x=iris["data"][:,3:]
y=(iris["target"] ==2).astype(np.int16)
# print(iris["data"])
# print(x)
# print(y)
# using thenlogistic regression classifier 
clf=LogisticRegression()
clf.fit(x,y)
example=clf.predict(([[2.6]]))
print(example)
# now we are using the matplotlob to plot the visualization
x_new=np.linspace(0,3,1000).reshape(-1,1)
# print(x_new)
y_prob=clf.predict_proba(x_new)
plt.plot(x_new,y_prob[:,1],"g-",label="verginica")
plt.show()