def bin_to_dec(bin):
    """
    Converts a binary string to its decimal representation.

    INPUT:
        bin: str
            A string representing a binary number

    OUTPUT:
        dec: int
            The decimal equivalent of the input binary string.
    """
    n = len(bin)
    dec = 0
    exp = 0
    for i in range(n-1, -1, -1):
        if bin[i] == "1":
            dec += 2**exp
        exp += 1

    return dec


def dec_to_bin(dec):
    """
    Converts a decimal number to its binary representation.

    INPUT:
        dec: int
            The decimal number to be converted.

    OUTPUT:
        bin: str
            A string representing the binary equivalent of the input decimal number.
    """
    bin = ""
    while dec > 0:
        bin += str(dec%2)
        dec //= 2

    return bin[::-1]


def read_population(route):
    """
    Reads the individuals of a population from a .txt document

    INPUT:
        route: string
            Path to the file

    OUTPUT:
        pop: list
            A list containing the individuals in the population
    """  
    f = open(r""+route, "r")

    aux = [row for row in f][0]
    aux = aux[1:-1]
    pop = []

    a = []
    flag = False
    for i in aux:   
        if i == "[": flag = True
        if i == "]": 
            flag = False
            pop.append(a)
            a = []
        if flag and (i == "1" or i == "0"):
            a.append(int(i))

    return pop


def hamming_distance(a, b):
    """
    Calculate the hamming distance between two strings a and b

    INPUT:
        a: string
        b: string

    OUTPUT:
        distance: int
            Return the hamming distance
    """
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]: distance += 1

    return distance


def total_variation_distance(F):
    """
    Calculate the total variation distance (statistical distance) between 
    distribution 'F' and the uniform distribution

    INPUT:
        F: dictionary
            Frequency of moves made by an individual

    OUTPUT:
        distance: int
            Return the total variation distance
    """

    distance = -1
    n = len(F)
    expected_value = sum([v for v in F.values()])/n

    for f in F.values():
        distance = max(distance, abs(expected_value-f))

    return distance