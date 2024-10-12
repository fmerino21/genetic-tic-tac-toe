import numpy
import random
import array
import pandas as pd

from deap import algorithms
from deap import base
from deap import creator
from deap import tools


from General.simulate_game import global_d
from Circuits.v5.circuit_v5 import evaluate_circuit_v5, get_size_circuit_v5
from Circuits.v4.circuit_v4 import evaluate_circuit_v4, get_size_circuit_v4
from Circuits.v3.circuit_v3 import evaluate_circuit_v3, get_size_circuit_v3
from Circuits.v2.circuit_v2 import evaluate_circuit_v2, get_size_circuit_v2
from Circuits.v1.circuit_v1 import evaluate_circuit_v1, get_size_circuit_v1

from General.fitness_function import *
from General.simulate_game import *

N_GAMES = 1000
COACH_MODE = "random"
CIRCUIT_VERSION = "v4"
FITNESS = "standard"    
PVP = False

def eval_solution(population, player): 
    if PVP == False:
        d = player_vs_coach(player, N_GAMES, COACH_MODE, CIRCUIT_VERSION)[0]
        if FITNESS == "standard": fitness_value = calculate_fitness_value_standard(d, [10, 0, -10, -10, 10])
        if FITNESS == "diversity": fitness_value = calculate_fitness_value_diversity(d, [10, 0, -10, -10, 10])
        return fitness_value, 
    else:
        #N_GAMES = 10
        d = player_vs_player(player, 10, population, CIRCUIT_VERSION)[0]
        if FITNESS == "standard": fitness_value = calculate_fitness_value_standard(d, [10, 0, -10, -10, 10])
        if FITNESS == "diversity": fitness_value = calculate_fitness_value_diversity(d, [10, 0, -10, -10, 10])
        return fitness_value,   
        


def main():
    #----------------- CONFIGURATION ----------------------

    IND_SIZE = get_size_circuit_v4()

    creator.create("FitnessMin", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, typecode='i', fitness=creator.FitnessMin)

    toolbox = base.Toolbox()

    toolbox.register("attr_int", random.choices, range(2), k=IND_SIZE, weights=[0.5, 0.5])

    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attr_int)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=10)
    
    #------------------------------------------------------#
    pop = toolbox.population(n=50)
    toolbox.register("evaluate", eval_solution, pop)


    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    RECOMBINATION_PROB = 0.7
    MUTATION_PROB = 0.2
    N_GENERATIONS = 2000
    
    log = algorithms.eaSimple(pop, toolbox, RECOMBINATION_PROB, 
                              MUTATION_PROB, N_GENERATIONS, stats=stats, halloffame=hof)
    
    return pop, stats, hof, log

if __name__ == "__main__":
    f = open("output.txt", "w")
    g = open("pop.txt", "w")

    pop,stats,hof,logbook=main()

    lines = []
    lines.append("".join([str(i) for i in hof[0]]))
    lines.append(str(global_d))

    f.write("\n".join(lines))

    pop_str = [list(p) for p in pop]
    g.write(str(pop_str))

    df_log = pd.DataFrame(logbook[1])
    df_log.to_csv('output.csv', index=False)