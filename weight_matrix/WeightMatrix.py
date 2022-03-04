HEIGHT = 32
WIDTH = 64
DEFAULT_BIAS = 6


class WeightMatrix:
    weight_matrix = []
    bias = DEFAULT_BIAS

    def __init__(self, text_input):
        if text_input is None:
            self.bias = DEFAULT_BIAS
            self.create_weight_matrix()

        elif len(text_input) == 0:
            self.create_weight_matrix()

        else:
            self.bias = int(text_input[0][:-1])
            for i in range(1, len(text_input)):
                self.weight_matrix.append(
                    list(map(int, text_input[i][:-1].replace('.', '0').replace('#', '1').split()))
                )

    def create_weight_matrix(self):
        self.weight_matrix = [[0] * WIDTH] * HEIGHT

    def __str__(self):
        return self.bias.__str__() + '\n' \
               + '\n'.join([''.join(['{} '.format(item) for item in row]) for row in self.weight_matrix])
