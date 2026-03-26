from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_and_save_model():
    # Load dataset
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # Train model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Save model
    joblib.dump(clf, "iris_model.pkl")
    print("✅ Model trained and saved as iris_model.pkl")

    # Print accuracy
    acc = clf.score(X_test, y_test)
    print(f"Model accuracy: {acc:.2f}")

if __name__ == "__main__":
    train_and_save_model()