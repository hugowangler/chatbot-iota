"""
The subjects that the chatbot can prompt the user about
"""
import random


subjects = [
    "Harry Potter",
    "Lord of the Rings",
    "Machine learning",
    "Python",
    "Jupyter Notebook",
    "Neural networks",
]


def get_subject() -> str:
    """ Returns a random subject """
    return subjects[random.randint(0, len(subjects) - 1)]


if __name__ == "__main__":
    print(get_subject())
