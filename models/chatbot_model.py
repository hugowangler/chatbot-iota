"""
Chatbot model module
"""
import pickle

import numpy as np
import torch
from torch import nn


class ChatbotModel(nn.Module):
    """ The model of the chatbot """

    def __init__(self, vocab_size=6764, vectorizer=None):
        super().__init__()
        self.vectorizer = vectorizer
        self.network = nn.Sequential(
            # input layer
            nn.Linear(vocab_size, 250),
            nn.ReLU(),
            # hidden layer
            nn.Linear(250, 30),
            nn.ReLU(),
            # output layer
            nn.Linear(30, 2),
        )

    def forward(self, x):  # pylint: disable=C0103
        """ Feedforward """
        return self.network(x)

    def predict(self, vec_x):
        """ Predicts the input x which is assumed to already be vectorized """
        with torch.no_grad():
            predictions = self.forward(vec_x)
            # Get the predicted category from each prediction
            return list(pred.argmax() for pred in predictions)

    def predict_str(self, str_x: str):
        """
        Vectorizes and predicts on the input str_x which is assumed to be a
        string
        """
        if not self.vectorizer:
            raise Exception(
                "ChatbotModel: Unable to predict on string input, vectorizer"
                + " is not stored in model."
            )

        vec_x = self.vectorizer.transform([str_x]).todense()
        tensor_x = torch.from_numpy(np.array(vec_x)).type(torch.FloatTensor)
        return self.predict(tensor_x)[0]

    def save_model(self, name="ann-model-amazon"):
        """
        Saves the pytorch models parameters to allow for later usage of the
        model.

        The saved models can be found in the ./models/saved-models folder.
        """
        path = f"saved-models/{name}.pth"
        # path = f"saved-models/{name}.pkl"
        torch.save(self.state_dict(), path)
        if self.vectorizer:
            # store the TFIDF for usage when transforming new user input
            pickle.dump(
                self.vectorizer, open("saved-models/tfidf_features.pkl", "wb")
            )
