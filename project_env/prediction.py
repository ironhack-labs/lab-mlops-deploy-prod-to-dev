import joblib
import numpy as np

def predict(sample):
    clf = joblib.load("iris_model.pkl")
    prediction = clf.predict([sample])
    return prediction

if __name__ == "__main__":
    # Example: sepal length, sepal width, petal length, petal width
    sample = [5.1, 3.5, 1.4, 0.2]
    print(f"Prediction for {sample}: {predict(sample)}")