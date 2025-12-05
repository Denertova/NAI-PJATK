import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"
cols = ["buying","maint","doors","persons","lug_boot","safety","class"]
df = pd.read_csv(url, names=cols)

X = df.drop("class", axis=1)
y = df["class"]

encoder = OneHotEncoder()
X_enc = encoder.fit_transform(X)

label_enc = LabelEncoder()
y_enc = label_enc.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X_enc, y_enc, test_size=0.2, random_state=42, stratify=y_enc)

kernels = ["linear", "rbf", "poly"]

for kernel in kernels:
    print("Kernel:", kernel)
    if kernel == "poly":
        clf = SVC(kernel=kernel, C=1.0, gamma='scale', degree=3)
    else:
        clf = SVC(kernel=kernel, C=1.0, gamma='scale')

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    print("-"*40)

    # --- Wizualizacja 2D po PCA ---
    pca = PCA(n_components=2)
    X_vis = pca.fit_transform(X_enc.toarray())
    plt.figure(figsize=(6,5))
    plt.title(f"SVM ({kernel}) - PCA 2D")
    plt.scatter(X_vis[:,0], X_vis[:,1], c=y_enc, cmap=plt.cm.Set1, edgecolor='k', s=50)
    plt.xlabel('PCA1')
    plt.ylabel('PCA2')
    plt.show()
