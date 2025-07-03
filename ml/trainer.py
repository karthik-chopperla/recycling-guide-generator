# ml/trainer.py

from logic.training_data_generator import generate_training_data
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class MaterialModelTrainer:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def train(self, num_samples=100):
        """
        Trains a text classification model using synthetic training data.
        Returns the trained model and vectorizer.
        """
        data = generate_training_data(num_samples)
        descriptions, labels = zip(*data)

        X = self.vectorizer.fit_transform(descriptions)
        self.model.fit(X, labels)

        return self.model, self.vectorizer
