import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import joblib
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/synthetic_data.csv')

# Preprocess data
X = df[['material_type', 'decomposition_time', 'source']]
y = df['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Evaluate model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(clf, 'model/decision_tree_model.joblib')
print("Model saved to 'model/decision_tree_model.joblib'")

# Visualize the decision tree
plt.figure(figsize=(20,10))
plot_tree(clf, filled=True, feature_names=['material_type', 'decomposition_time', 'source'], class_names=clf.classes_)
plt.savefig('app/static/images/decision_tree.png')
print("Decision tree plot saved to 'app/static/images/decision_tree.png'")