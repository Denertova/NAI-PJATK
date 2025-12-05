# Decision Tree and SVM

**Problem description**
This repository contains experiments that train and evaluate Decision Tree and Support Vector Machine (SVM)
classifiers on two datasets:
1. **Boston housing** (provided in `abalone`) — converted from regression to a binary classification problem:
   - Target `MEDV` (median value) was thresholded at the median to create classes `low` / `high` house price.
2. **Wine (UCI)** — a multiclass classification dataset (3 classes) from UCI / scikit-learn.

**Author:** Klaudia Denert - s29276

**References**
- Ulqinaku, M., Ktona, A. *Analysis of Depth of Entropy and GINI Index Based Decision Trees for Predicting Diabetes.* (Paper supplied). https://jns.edu.al/wp-content/uploads/2024/01/M.UlqinakuA.Ktona-FINAL.pdf
- Machine Learning Mastery — Standard Datasets. https://machinelearningmastery.com/standard-machine-learning-datasets/
- UCI Wine dataset. https://archive.ics.uci.edu/ml/datasets/wine
- Scikit-learn documentation. https://scikit-learn.org/

**Instructions to run**

You can run the training script with:
```
python train_and_eval.py
```

