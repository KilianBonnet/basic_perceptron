from os import listdir
from os.path import isfile, join

from input_manager.TrainingInput import TrainingInput

TRAINING_PATH = "./training/"


def read_inputs():
    training_files = [f for f in listdir(TRAINING_PATH) if isfile(join(TRAINING_PATH, f))]

    for training_file in training_files:
        text_file = open(TRAINING_PATH + training_file, "r")
        training_input = TrainingInput(text_file.readlines())
        print(training_input.input_matrix)
