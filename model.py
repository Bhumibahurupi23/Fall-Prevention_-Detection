from sklearn.tree import DecisionTreeClassifier

X = [[5],[7],[20],[18],[6],[22],[4]]
y = [0,0,1,1,0,1,0]

model = DecisionTreeClassifier()
model.fit(X, y)

def predict_fall(acc):
    return model.predict([[acc]])[0]