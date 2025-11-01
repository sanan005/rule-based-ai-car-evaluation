import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from flat_classifier import flat_classify
from hierarchical_classifier import hierarchical_classify

# Load data
cols = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
data = pd.read_csv('car.data', names=cols)

# Split
X = data.drop('class', axis=1)
y = data['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Predict
y_pred_flat = X_test.apply(flat_classify, axis=1)
y_pred_hier = X_test.apply(hierarchical_classify, axis=1)

# Results
print("FLAT SYSTEM")
print("Accuracy:", accuracy_score(y_test, y_pred_flat))
print(classification_report(y_test, y_pred_flat))

print("\nHIERARCHICAL SYSTEM")
print("Accuracy:", accuracy_score(y_test, y_pred_hier))
print(classification_report(y_test, y_pred_hier))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred_hier)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=sorted(y.unique()), yticklabels=sorted(y.unique()))
plt.title('Hierarchical System Confusion Matrix')
plt.ylabel('True')
plt.xlabel('Predicted')
plt.savefig('confusion_matrix.png')
