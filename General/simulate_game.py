from random import randint
from General.coach_models import check_victory, check_move, update_state, generate_move_fixed, generate_move_random

from Circuits.v1.circuit_v1 import evaluate_circuit_v1
from Circuits.v2.circuit_v2 import evaluate_circuit_v2
from Circuits.v3.circuit_v3 import evaluate_circuit_v3
from Circuits.v4.circuit_v4 import evaluate_circuit_v4
from Circuits.v5.circuit_v5 import evaluate_circuit_v5


global_d = {}

def player_vs_coach(player, n_games, coach_mode, circuit_version):
    """
    Simulation process to obtain the performance metrics of a player in the 
    random or fixed training model

    INPUT:
        player: list
            List of binary weigths representing a player
        n_games: int
            Number of games to be simulated
        coach_mode: str
            String representing the training model to be used (fixed or random)
        circuit_version: str
            Version of the circuit to be evaluated

    OUTPUT:
        otuput: dict
            Dictionary containing the performance metrics of the player 

    """
    moves = []

    player_wins = 0     # 10
    draws = 0
    player_outside_move = 0
    player_overlapped_move = 0
    coach_wins = 0     # 01
    for _ in range(n_games):
        temp_moves = []
        if coach_mode == "fixed": coach_r = randint(0, 3) 

        turn = 0
        state = "000000000000000000"
        while True:
            if turn == 9: 
                draws += 1
                temp_moves.append("draw")
                break

            victory = check_victory(state)
            if victory[0] == True:
                if victory[1] == "10": 
                    player_wins += 1
                    temp_moves.append("player_win")
                else: 
                    coach_wins += 1
                    temp_moves.append("coach_win")
                break
            
            # Player
            if turn % 2 != 0:
                # Generates move
                if circuit_version == "v1": move = evaluate_circuit_v1(state, player)
                if circuit_version == "v2": move = evaluate_circuit_v2(state, player)
                if circuit_version == "v3": move = evaluate_circuit_v3(state, player)
                if circuit_version == "v4": move = evaluate_circuit_v4(state, player)
                if circuit_version == "v5": move = evaluate_circuit_v5(state, player)

                temp_moves.append(move)
                
                if move not in global_d: global_d[move] = 1
                else: global_d[move] += 1
                
                # Check the validity of the move
                if move >= 9: 
                    player_outside_move += 1
                    temp_moves.append("player_outside_move")
                    break
                if check_move(state, move) == False: 
                    player_overlapped_move += 1
                    temp_moves.append("player_overlapped_move")
                    break
                else:
                    # Update game state
                    state = update_state(state, move, '10')

                turn += 1

            # Trainer
            else:
                if coach_mode == "random": move = generate_move_random(state)
                if coach_mode == "fixed": move = generate_move_fixed(state, coach_r)

                state = update_state(state, move, '01')

                turn += 1

        moves.append(temp_moves)
    
    return {
            "Player wins": player_wins, 
            "Coach wins": coach_wins,
            "Player outside moves": player_outside_move,
            "Player overlapped moves": player_overlapped_move,
            "Draws": draws
            }, moves


def player_vs_player(player1, n_games, population, circuit_version):
    """
    Simulation process to obtain the performance metrics of a player in the 
    player vs. player training model

    INPUT:
        player1: list
            List of binary weigths representing a player
        n_games: int
            Number of games to be simulated
        population: list
            List containing all the individuals in the population of the genetic algorithm
        circuit_version: str
            Version of the circuit to be evaluated

    OUTPUT:
        otuput: dict
            Dictionary containing the performance metrics of the player 

    """
    moves = []

    player1_wins = 0 
    player1_outside_moves = 0
    player1_overlapped_moves = 0

    player2_wins = 0 
    player2_outside_moves = 0
    player2_overlapped_moves = 0

    draws = 0

    for player2 in population:
        for _ in range(n_games):
            temp_moves = []

            turn = 0
            state = "000000000000000000"
            while True:
                if turn == 9: 
                    draws += 1
                    temp_moves.append("draw")
                    break

                victory = check_victory(state)
                if victory[0] == True:
                    if victory[1] == "10": 
                        player1_wins += 1
                        temp_moves.append("player_win")
                    else: 
                        player2_wins += 1
                        temp_moves.append("coach_win")
                    break
                
                # Player 1
                if turn % 2 != 0:
                    if circuit_version == "v1": move = evaluate_circuit_v1(state, player1)
                    if circuit_version == "v2": move = evaluate_circuit_v2(state, player1)
                    if circuit_version == "v3": move = evaluate_circuit_v3(state, player1)
                    if circuit_version == "v4": move = evaluate_circuit_v4(state, player1)
                    if circuit_version == "v5": move = evaluate_circuit_v5(state, player1)

                    temp_moves.append(move)

                    if move >= 9: 
                        player1_outside_moves += 1
                        temp_moves.append("player_outside_move")
                        break
                    if check_move(state, move) == False: 
                        player1_overlapped_moves += 1
                        temp_moves.append("player_overlapped_move")
                        break
                    else:
                        # Update game state
                        state = update_state(state, move, '10')

                    turn += 1

                # Player 2
                else:
                    if circuit_version == "v1": move = evaluate_circuit_v1(state, player2)
                    if circuit_version == "v2": move = evaluate_circuit_v2(state, player2)
                    if circuit_version == "v3": move = evaluate_circuit_v3(state, player2)
                    if circuit_version == "v4": move = evaluate_circuit_v4(state, player2)
                    if circuit_version == "v5": move = evaluate_circuit_v5(state, player2)

                    if move >= 9: 
                        player2_outside_moves += 1
                        break
                    if check_move(state, move) == False: 
                        player2_overlapped_moves += 1
                        break
                    else:
                        state = update_state(state, move, '01')

                    turn += 1

            moves.append(temp_moves)

    return {
            "Player wins": player1_wins, 
            "Coach wins": player2_wins,
            "Player outside moves": player1_outside_moves,
            "Player overlapped moves": player1_overlapped_moves,
            "Draws": draws
            }, moves
