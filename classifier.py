from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
from matplotlib import style
import matplotlib.pyplot as plt
import pandas as pd
import ipdb

class_weight = {0: 0.2, 1: 0.2, 2: 0.6, 3: 0.4, 4: 0.2, 5: 0.45, 6: 0.4, 7: 0.25, 8: 0.7, 9: 1,
                10: 0.8, 11: 0.6}

# read dataset
df = pd.read_excel("Emergency_casebase.xls")
X = np.array(df.astype(float))
df_label = pd.read_excel("classes.xls")
y = np.array(df_label)

model = LogisticRegression(solver='liblinear', multi_class='ovr', random_state=0).fit(X, y)
input2 = np.array([[1, 0, 15, 1, 1, 0, 0, 0],
                   [0, 0, 62, 1, 0, 1, 0, 1],
                   [0, 2, 62, 1, 1, 0, 0, 0],
                   [1, 0, 62, 1, 3, 1, 0, 0],
                   [2, 0, 100, 0, 5, 0, 1, 1],
                   [3, 0, 225, 1, 1, 1, 0, 1],
                   [0, 2, 15, 1, 1, 0, 0, 0],
                   [0, 1, 30.5, 1, 3, 1, 2, 1],
                   [0, 1, 15, 1, 5, 1, 0, 1],
                   [1, 1, 50, 1, 5, 1, 0, 1],
                   [1, 1, 50, 1, 5, 1, 0, 1],
                   [1, 0, 27, 1, 1, 0, 1, 0]])

y_predict = model.predict(input2)
print(model.score(input2, y))
ipdb.set_trace()

# count = 0
# for i in range(12):
#     count += model.predict_proba(input2)[11][i]
# print(count)




