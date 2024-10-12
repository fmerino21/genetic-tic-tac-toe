import random

def generate_move_random(state):
    """
    Generates a random valid move in the board

    INPUT:
        state: str
            A binary string representing a game state

    OUTPUT:
        move: str
            The move generated

    """
    move = random.randint(0,8)

    while check_move(state, move) == False: 
        move = random.randint(0,8)

    return move


def generate_move_fixed(state, mode):
    """
    Generates a valid move from a predefined game strategy
 
    INPUT:
        state: str
            A binary string representing a game state
        mode: int
            mode = {0, 1, 2}. Specific strategy to be used

    OUTPUT:
        move: str
            The move generated

    """
    if mode == 0:
        # Secondary diagonal 
        if state[4:6] == "00": return 2
        if state[8:10] == "00": return 4
        if state[12:14] == "00": return 6

        # Second column
        if state[2:4] == "00": return 1
        if state[8:10] == "00": return 4
        if state[14:16] == "00": return 7

        # Draw
        if state[8:10] == "00": return 4
        if state[2:4] == "00": return 1
        if state[:2] == "00": return 0
        if state[10:12] == "00": return 5

        # Second column
        if state[12:14] == "00": return 6
        if state[6:8] == "00": return 3
        if state[:2] == "00": return 0

        # First column
        if state[6:8] == "00": return 3
        if state[:2] == "00": return 0
        if state[12:14] == "00": return 6

        # Third column
        if state[4:6] == "00": return 2
        if state[10:12] == "00": return 5
        if state[16:18] == "00": return 8
    elif mode == 1:
        # First column
        if state[6:8] == "00": return 3
        if state[:2] == "00": return 0
        if state[12:14] == "00": return 6

        # Second column
        if state[12:14] == "00": return 6
        if state[6:8] == "00": return 3
        if state[:2] == "00": return 0

        # Third column
        if state[4:6] == "00": return 2
        if state[10:12] == "00": return 5
        if state[16:18] == "00": return 8
    elif mode == 2:
        # Second column
        if state[2:4] == "00": return 1
        if state[8:10] == "00": return 4
        if state[14:16] == "00": return 7

        # Draw
        if state[8:10] == "00": return 4
        if state[2:4] == "00": return 1
        if state[:2] == "00": return 0
        if state[10:12] == "00": return 5

        # Secondary diagonal 
        if state[4:6] == "00": return 2
        if state[8:10] == "00": return 4
        if state[12:14] == "00": return 6

        # Third column
        if state[4:6] == "00": return 2
        if state[10:12] == "00": return 5
        if state[16:18] == "00": return 8

        # Second column
        if state[12:14] == "00": return 6
        if state[6:8] == "00": return 3
        if state[:2] == "00": return 0

        # First column
        if state[6:8] == "00": return 3
        if state[:2] == "00": return 0
        if state[12:14] == "00": return 6
    #else:
        #return generate_move_random(state)


# Validar el estado de victoria en el estado actual del tablero 
# State: Cadena(String) binaria de 18 bits
# Retorna una tupla indicando si se cumple la condicion de victoria o no

def check_victory(state):
    """
    Checks whether the player or the trainer has already won the game
 
    INPUT:
        state: str
            A binary string representing a game state

    OUTPUT:
        output: (bool, str)
            A pair representing the victory state and the corresponding winner, if applicable
            (False, '00) -> No winner

    """
    # vertical
    if state[:2] == state[6:8] and state[6:8] == state[12:14] and state[:2] != "00" and state[:2] != "11": return (True, state[:2])
    if state[2:4] == state[8:10] and state[8:10] == state[14:16] and state[2:4] != "00" and state[2:4] != "11": return (True, state[2:4])
    if state[4:6] == state[10:12] and state[10:12] == state[16:18] and state[4:6] != "00" and state[4:6] != "11": return (True, state[4:6])

    # horizontal
    if state[:2] == state[2:4] and state[2:4] == state[4:6] and state[:2] != "00" and state[:2] != "11": return (True, state[:2])
    if state[6:8] == state[8:10] and state[8:10] == state[10:12] and state[6:8] != "00" and state[6:8] != "11": return (True, state[6:8])
    if state[12:14] == state[14:16] and state[14:16] == state[16:18] and state[12:14] != "00" and state[12:14] != "11": return (True, state[12:14])

    # diagonal
    if state[:2] == state[8:10] and state[8:10] == state[16:18] and state[:2] != "00" and state[:2] != "11": return (True, state[:2])
    if state[4:6] == state[8:10] and state[8:10] == state[12:14] and state[4:6] != "00" and state[4:6] != "11": return (True, state[4:6])

    return (False, '00')


# Validar si una jugada es valida
# state: Cadena (String) binaria de 18 bits
# move: Entero en el intervalo [0, 8]
# Retorna si una jugada es valida o no

def check_move(state, move):
    """
    Checks whether a move is valid or not
 
    INPUT:
        state: str
            A binary string representing a game state
        move: int
            Integer representing the move to be made

    OUTPUT:
        output: bool
            A boolean representing the validity of the move

    """
    if move == 0 and (state[0:2] == '00' or state[0:2] == '11'): return True
    if move == 1 and (state[2:4] == '00' or state[2:4] == '11'): return True
    if move == 2 and (state[4:6] == '00' or state[4:6] == '11'): return True
    if move == 3 and (state[6:8] == '00' or state[6:8] == '11'): return True
    if move == 4 and (state[8:10] == '00' or state[8:10] == '11'): return True
    if move == 5 and (state[10:12] == '00' or state[10:12] == '11'): return True
    if move == 6 and (state[12:14] == '00' or state[12:14] == '11'): return True
    if move == 7 and (state[14:16] == '00' or state[14:16] == '11'): return True
    if move == 8 and (state[16:18] == '00' or state[16:18] == '11'): return True
    return False


# Actualiza el estado del tablero en base a un jugada
# state: Cadena (String) binaria de 18 bits
# move: Entero en el intervalo [0, 8]
# placer: Cadena (String) binaria de 2 bits
# Retorna el estado actualziado del tablero

def update_state(state, move, player):
    """
    Updates the game state
 
    INPUT:
        state: str
            A binary string representing a game state
        move: int
            Integer representing the move to be made
        player: str
            String representing the player that made the move (Player or trainer)

    OUTPUT:
        state: str
            String representing the updated game state

    """
    if move == 0: state = player + state[2:]
    if move == 1: state = state[:2] + player + state[4:]
    if move == 2: state = state[:4] + player + state[6:]
    if move == 3: state = state[:6] + player + state[8:]
    if move == 4: state = state[:8] + player + state[10:]
    if move == 5: state = state[:10] + player + state[12:]
    if move == 6: state = state[:12] + player + state[14:]
    if move == 7: state = state[:14] + player + state[16:]
    if move == 8: state = state[:16] + player
    return state