from General.auxiliar import bin_to_dec
from General.circuit_utils import evaluate_cells, general_XOR

INITIAL_BITS = 18
LOGIC_CELL2_OUTPUT = 4

def evaluate_circuit_v3(state, weights):
    output = ""

    SIZE_LAYER_1 = 4

    # ------------------------- Layer 0 -------------------------------------------
    layer0 = [[i, i+1] for i in range(0,17,2)]
    layer0_output = evaluate_cells(layer0, state)
    layer0_output = [j for i in layer0_output for j in i]
    # -----------------------------------------------------------------------------
    
    # ------------------------- Layer 1 -------------------------------------------
    current_w = 0

    XOR = [[] for i in range(SIZE_LAYER_1)]

    for i in range(len(XOR)):
        for j in range(len(layer0_output)):
            if weights[current_w] == 1: XOR[i].append(layer0_output[j])
            current_w += 1

    layer1_output = [general_XOR(i) for i in XOR]
    # -----------------------------------------------------------------------------

    output = "".join(layer1_output)
    output = bin_to_dec(output)
    return output


def get_size_circuit_v3():
    return 9*4*4