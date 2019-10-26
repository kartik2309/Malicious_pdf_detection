from pandas import read_csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from feature_extraction import feature_extraction

df = read_csv('pdfdataset_n.csv')
X = df.iloc[:, 0: 21]
y = df.iloc[:, 21]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

print("---Random Forest---")
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acs = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print("Accuracy:", acs)
print("\nConfusion Matrix:\n", cm)


path = '/Users/kartik/Desktop/review2.pdf'
features = feature_extraction(path)
result = clf.predict(features)
print(result)
