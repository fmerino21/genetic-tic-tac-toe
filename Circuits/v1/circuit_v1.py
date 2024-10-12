from General.auxiliar import bin_to_dec
from General.circuit_utils import evaluate_cells, general_XOR, logic_cell

INITIAL_BITS = 18
LOGIC_CELL2_OUTPUT = 4

def evaluate_circuit_v1(state, weights):
    output = ""

    SIZE_LAYER_1 = 4
    SIZE_LAYER_3 = 4
    SIZE_WEIGHTS_1 = ((INITIAL_BITS//2)*LOGIC_CELL2_OUTPUT)*(SIZE_LAYER_1)

    # ------------------------- Layer 0 -------------------------------------------
    layer0 = [[i, i+1] for i in range(0,17,2)]
    layer0_output = evaluate_cells(layer0, state) 
    layer0_output = [j for i in layer0_output for j in i]
    # -----------------------------------------------------------------------------

    # ------------------------- Layer 1 -------------------------------------------
    weights_1 = weights[0: SIZE_WEIGHTS_1]
    current_w = 0
    
    XOR_1 = [[] for i in range(SIZE_LAYER_1)]

    for i in range(len(XOR_1)):
        for j in range(len(layer0_output)):
            if weights_1[current_w] == 1: XOR_1[i].append(layer0_output[j])
            current_w += 1

    layer1_output = [general_XOR(i) for i in XOR_1]
    # -----------------------------------------------------------------------------

    # ------------------------- Layer 2 -------------------------------------------
    out_1 = logic_cell([layer1_output[0], layer1_output[1]])
    out_2 = logic_cell([layer1_output[2], layer1_output[3]])

    layer2_output = out_1 + out_2
    # -----------------------------------------------------------------------------

    # ------------------------- Layer 3 -------------------------------------------
    weights_2 =  weights[SIZE_WEIGHTS_1:]
    current_w = 0

    XOR_2 = [[] for i in range(SIZE_LAYER_3)]

    for i in range(len(XOR_2)):
        for j in range(len(layer2_output)):
            if weights_2[current_w] == 1: XOR_2[i].append(layer2_output[j])
            current_w += 1

    layer3_output = [general_XOR(i) for i in XOR_2]
    # -----------------------------------------------------------------------------

    output = "".join(layer3_output)
    output = bin_to_dec(output)
    return output


def get_size_circuit_v1():
    layer_1 = 9*4*4
    layer_2 = 2*4*4
    return layer_1 + layer_2