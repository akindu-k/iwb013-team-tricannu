import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

class TaskAssignmentModel:
    def __init__(self):
        self.model = LogisticRegression()
        self.vectorizer = TfidfVectorizer()

    def train(self, X, y):
        """Train the model on the given data."""
        X_vec = self.vectorizer.fit_transform(X)
        self.model.fit(X_vec, y)

    def predict(self, task):
        """Predict the assigned employee for a task."""
        task_vec = self.vectorizer.transform([task])
        return self.model.predict(task_vec)

    def save_model(self, file_path):
        """Save the trained model to a file."""
        with open(file_path, 'wb') as f:
            pickle.dump((self.vectorizer, self.model), f)

    def load_model(self, file_path):
        """Load the trained model from a file."""
        with open(file_path, 'rb') as f:
            self.vectorizer, self.model = pickle.load(f)
