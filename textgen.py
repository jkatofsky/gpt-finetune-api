from settings import TRAINING_EPOCHS
from textgenrnn import textgenrnn
import os


def train(training_strings):
    model = textgenrnn()
    model.train_on_texts(
        training_strings,
        num_epochs=TRAINING_EPOCHS,
        verbose=0 if os.getenv("SANIC_ACCESS_LOG") else 1,
        gen_epochs=0, save_epochs=0)
    return model


def generate(model: textgenrnn, prompt, max_length, temperature):
    output = model.generate(prefix=prompt,
                            max_gen_length=max_length,
                            temperature=temperature,
                            return_as_list=True)[0]
    return output
