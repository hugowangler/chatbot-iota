"""
The module used for analyzis of user input
"""

import pickle
import os

import torch

from models.chatbot_model import ChatbotModel


class Model:
    """
    The model consisting of the chatbot model which can be used to predict new
    user input using the pre-trained model
    """

    def __init__(self, model_path: str, tfidf_path: str = None):
        """
        Loads the model with the pretrained state from the specified path along
        with the TFIDF of the training vocabulary.
        """
        if tfidf_path:
            try:
                tfidf_file = open(tfidf_path, "rb")
            except OSError as tfidf_missing:
                raise Exception(
                    "TFIDF features could not be found at the specified "
                    + f"path='{tfidf_path}'"
                ) from tfidf_missing
            with tfidf_file:
                self.tfidf = pickle.load(tfidf_file)

        if not os.path.isfile(model_path):
            raise Exception(
                "Pretrained model is not saved at the specified "
                + f"path='{model_path}'"
            )

        self.model = ChatbotModel(vectorizer=self.tfidf)
        self.model.load_state_dict(torch.load(model_path))

    def predict(self, txt: str) -> bool:
        """
        Feeds the pretrained network with the input and returns a boolean
        representing the prediction, false is negative and true is positive.
        """
        return bool(self.model.predict_str(txt))
