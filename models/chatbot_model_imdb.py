"""
Chatbot model module
"""
from torch import nn

from chatbot_model import ChatbotModel


class ChatbotModelImdb(ChatbotModel):
    """ The model of the chatbot """

    def __init__(self, vocab_size=7305, vectorizer=None):
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
