
from sklearn import datasets
import pandas as pd
from sklearn.svm import SVC
import pickle


iris = datasets.load_iris()
X = iris.data  # we only take the first two features.
y = iris.target
# print (X)
df = pd.DataFrame(data=X,columns=iris.feature_names)
df['target'] = y
# print (df)
df = df.sample(frac=1).reset_index(drop=True)
clf =SVC(probability=True)
clf.fit(df.drop(columns='target'),df.target)

filename = 'iris_model.sav'
pickle.dump(clf, open(filename, 'wb'))
