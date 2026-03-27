from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load and split the data
def load_data():
    iris = load_iris()
    X = iris.data
    y = iris.target
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Train and save the model
def train():
    X_train, X_test, y_train, y_test = load_data()
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    joblib.dump(model, 'iris_model.pkl')
    print("✅ Model trained and saved as iris_model.pkl")

# Predict using a sample
def predict(sample):
    model = joblib.load('iris_model.pkl')
    prediction = model.predict([sample])
    print(f"🧠 Predicted class: {prediction[0]}")

if __name__ == "__main__":
    train()
    sample_input = [5.1, 3.5, 1.4, 0.2]
    predict(sample_input)
