UNDEFINED = -1


class TrainingInput:
    expected_weight = UNDEFINED
    input_matrix = []

    def __init__(self, text_input):
        if text_input is None:
            return

        if len(text_input) == 0:
            return

        self.expected_weight = int(text_input[0][:-1])
        for i in range(1, len(text_input)):
            self.input_matrix.append(list(map(int, text_input[i][:-1].replace('.', '0').replace('#', '1').split())))