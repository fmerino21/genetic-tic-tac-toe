def general_XOR(aux):
    """
    Computes the XOR of all bits in a given string of binary digits.

    INPUT:
        aux: str
            A string containing binary digits

    OUTPUT:
        output: str
            A string representing the XOR result of the input bits
    """
    XOR = 0
    for bit in aux: 
        XOR ^= int(bit)

    output = str(XOR)
    return output


def logic_cell(input):
    """
    Evaluates a logic cell 

    INPUT:
        input: str
            A string containing binary digits

    OUTPUT:
        output: list
            A list containing the evaluation of the logic cell
    """
    output_1 = 1
    output_2 = int(input[0])
    output_3 = int(input[0]) & int(input[1])
    output_4 = int(input[1]) 

    return [output_1, output_2, output_3, output_4]


def logic_cell_2(input, state):
    """
    Evaluates a logic cell receiving the input from a game state

    INPUT:
        input: str
            A string containing binary digits
        state: str
            A binary string representing a game state

    OUTPUT:
        output: list
            A list containing the evaluation of the logic cell
    """
    output_1 = 1
    output_2 = int(state[input[0]])
    output_3 = int(state[input[0]]) & int(state[input[1]])
    output_4 = int(state[input[1]])

    return [output_1, output_2, output_3, output_4]


def evaluate_cells(layer, state):
    """
    Evaluates the first layer in a logic circuit receiving the input from a game state

    INPUT:
        layer: str
            A string containing binary string
        state: str
            A binary string representing a game state

    OUTPUT:
        output: list
            A list containing the evaluation of the cell
    """
    output = []
    for i in layer:
        output.append(logic_cell_2(i, state))

    return output

def evaluate_cells_2(layer):
    """
    Evaluates the first layer in a logic circuit

    INPUT:
        layer: str
            A string containing binary string

    OUTPUT:
        output: list
            A list containing the evaluation of the cell
    """
    output = []
    for i in layer:
        output.append(logic_cell(i))

    return output


def logic_cell_3(input, state):
    """
    Evaluates a 3-logic-cell receiving the input from a game state

    INPUT:
        input: str
            A string containing binary digits
        state: str
            A binary string representing a game state

    OUTPUT:
        output: list
            A list containing the evaluation of the logic cell
    """
    output_1 = 1

    output_2 = int(state[input[0]])
    output_3 = int(state[input[1]])
    output_4 = int(state[input[2]])

    output_5 = int(state[input[0]]) & int(state[input[1]])
    output_6 = int(state[input[0]]) & int(state[input[2]])
    output_7 = int(state[input[1]]) & int(state[input[2]])

    output_8 = int(state[input[0]]) & int(state[input[1]]) & int(state[input[2]])

    return [output_1, output_2, output_3, output_4, 
            output_5, output_6, output_7, output_8]


def evaluate_cells_3(layer, state):
    """
    Evaluates the first layer in a logic circuit receiving the input from a game state
    and using a 3-logic-cell

    INPUT:
        layer: str
            A string containing binary string
        state: str
            A binary string representing a game state

    OUTPUT:
        output: list
            A list containing the evaluation of the cell
    """
    output = []
    for i in layer:
        output.append(logic_cell_3(i, state))

    return output