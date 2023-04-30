from sklearn.neural_network import MLPClassifier

class MLPModel:
    def __init__(self):
        self.model = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', max_iter=1000)

    def train(self, X, y):
        self.model.fit(X, y)

    def fit(self, X, y):
        self.train(X, y)

    def predict(self, X):
        return self.model.predict(X)