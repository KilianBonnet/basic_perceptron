from file_manager.io_manager import *

TRAINING_PATH = "./training/data/"
WEIGHT_MATRIX_PATH = "./weight_matrix/data/"
WEIGHT_MATRIX_NAME = "rectangle"


def main():
    training_inputs = read_input_datas(TRAINING_PATH)
    weight_matrix = read_weight_matrix_data(WEIGHT_MATRIX_PATH, WEIGHT_MATRIX_NAME)
    write_weight_matrix(WEIGHT_MATRIX_PATH, WEIGHT_MATRIX_NAME, weight_matrix)


if __name__ == '__main__':
    main()
