from os import listdir
from os.path import isfile, join
from pathlib import Path

from training.TrainingInput import TrainingInput
from weight_matrix.WeightMatrix import WeightMatrix


def read_input_datas(training_path):
    """
    For a given training path, will return the list of associated TrainingInput objects.
    """
    # Getting all files names from the training folder situated in TRAINING_PATH.
    training_file_names = [f for f in listdir(training_path) if isfile(join(training_path, f))]
    training_inputs = []  # List of each TrainingInput.

    # Create a TrainingInput object for each training input file.
    for training_file_name in training_file_names:
        text_file = open(training_path + training_file_name, "r")
        training_inputs.append(TrainingInput(text_file.readlines()))
        text_file.close()

    return training_inputs


def read_weight_matrix_data(weight_matrix_path, name):
    """
    For a given matrix data path and name, will return the associated WeightMatrix object.
    """
    path = Path(weight_matrix_path + name + "-weight_matrix.txt")

    if path.is_file():
        text_file = open(path, "r")
        return WeightMatrix(text_file.readlines())

    return WeightMatrix(None)


def write_weight_matrix(weight_matrix_path, name, weight_matrix):
    """
    For a given matrix object, will write the associated WeightMatrix object as 'name' in the given 'weight_matrix_path'.
    """
    f = open(weight_matrix_path + name + "-weight_matrix.txt", "w")
    f.write(weight_matrix.__str__())
    f.close()
