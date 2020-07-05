from textgenrnn import textgenrnn
import os

# NOTE: this code is contingent on a line tweak in the textgenrnn module
# the issue: https://github.com/minimaxir/textgenrnn/issues/197
# my PR for the fix: https://github.com/minimaxir/textgenrnn/pull/199

# TODO: verbose = 0 on prod


BASE_DIR = os.getcwd()


def _get_model_dir(model_id):
    return 'tmp/%s' % model_id


def train(model_id, training_strings):
    model_dir = _get_model_dir(model_id)
    os.mkdir(model_dir)
    os.chdir(model_dir)

    textgen = textgenrnn()
    textgen.train_on_texts(training_strings, num_epochs=3, gen_epochs=0)
    textgen.save(weights_path="weights.hdf5")

    os.chdir(BASE_DIR)


def generate(model_id, options):
    model_dir = _get_model_dir(model_id)
    os.chdir(model_dir)

    prompt = options.get('prompt', None)
    num_words = options.get('num_words', 300)
    temperature = options.get('temperature', 0.5)

    textgen = textgenrnn("weights.hdf5")
    output = textgen.generate(prefix=prompt,
                              max_gen_length=num_words,
                              temperature=temperature,
                              return_as_list=True)[0]

    os.chdir(BASE_DIR)
    return output
