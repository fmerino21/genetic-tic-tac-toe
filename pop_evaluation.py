from General.simulate_game import player_vs_coach, player_vs_player
from General.auxiliar import read_population, hamming_distance
from General.fitness_function import calculate_fitness_value_standard
 

N_GAMES = 1000

#population = read_population("pop.txt")

s = ""
population = [[int(i) for i in s]]
print(population)

unique = []
for p in population:
    count = 0
    for j in unique:
        if hamming_distance(p, j) != 0: count += 1

    if count == len(unique): unique.append(p)

print("Unique individuals", len(unique))

individuals = []
for p in unique:
    d = player_vs_coach(p, N_GAMES, "fixed", "v3")[0]
    fitness_value = calculate_fitness_value_standard(d, [10, 0, -10, -10, 10])
    individuals.append([fitness_value, p])

individuals.sort(reverse=True)
print(individuals)

print("\n--------------------------------------\n")
p = individuals[0][1]
ans = player_vs_coach(p, N_GAMES, "fixed", "v3")
print(ans[0])
d = ans[0]
print(f"fitness value: {d['Player wins']*10 + d['Coach wins']*0 + d['Player outside moves']*-10 + d['Player overlapped moves']*-10 + d['Draws']*10}")

moves = ans[1]
d = {}
for i in moves:
    for j in range(len(i)-1):
        if i[j] not in d: d[i[j]] = 1
        else: d[i[j]] += 1

print(f"Moves:  {d}")
print(f"len moves {len(d)}")


d_draw = {}

for game in ans[1]:
    if len(game) > 0:
        if game[-1] == "draw": 
            print(game)
        
            game = [str(i) for i in game[:-1]]
            idx = ",".join(game)
            if idx not in d_draw: d_draw[idx] = 1
            else: d_draw[idx] += 1


d_win = {}
print("\n--------------------------------------\n")
for game in ans[1]:
    if len(game) > 0:
        if game[-1] == "player_win": 
            print(game)

            game = [str(i) for i in game[:-1]]
            idx = ",".join(game)
            if idx not in d_win: d_win[idx] = 1
            else: d_win[idx] += 1


print("\n--------------------------------------\n")
for game in ans[1]:
    if len(game) > 0:
        if game[-1] == "coach_win": print(game)



print(d_draw)
print(d_win)
