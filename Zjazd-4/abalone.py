import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from utilities import visualize_classifier

input_file = 'abalone.txt'
df = pd.read_csv(input_file, header=None)

sex_mapping = {'M': 0, 'F': 1, 'I': 2}
df[0] = df[0].map(sex_mapping)

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

y = (y >= 10).astype(int)

X_vis = X[:, :2]

class_0 = X_vis[y == 0]
class_1 = X_vis[y == 1]

plt.figure()
plt.scatter(class_0[:, 0], class_0[:, 1], s=75, facecolors='black',
            edgecolors='black', linewidth=1, marker='x')
plt.scatter(class_1[:, 0], class_1[:, 1], s=75, facecolors='white',
            edgecolors='black', linewidth=1, marker='o')
plt.title('Input data')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(
    X_vis, y, test_size=0.25, random_state=5
)

params = {'random_state': 0, 'max_depth': 8}
classifier = DecisionTreeClassifier(**params)
classifier.fit(X_train, y_train)

visualize_classifier(classifier, X_train, y_train, 'Training dataset')
y_test_pred = classifier.predict(X_test)
visualize_classifier(classifier, X_test, y_test, 'Test dataset')

class_names = ['Class-0', 'Class-1']
print("\n" + "#"*40)
print("\nClassifier performance on training dataset\n")
print(classification_report(y_train, classifier.predict(X_train), target_names=class_names))
print("#"*40 + "\n")

print("#"*40)
print("\nClassifier performance on test dataset\n")
print(classification_report(y_test, y_test_pred, target_names=class_names))
print("#"*40 + "\n")
