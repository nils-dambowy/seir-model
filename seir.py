import random
import time




def decision(prob):
    return random.random() < prob


def susceptible(x, pop, expo, infec, reco):
    """
    Probability of transmission: b
    avg. number of contacts (per person): c

    b * c = transmission rate
    """
    tr = 0.3
    print(pop)

    if decision(tr):
        print("{} is exposed!".format(str(x)))
        pop -= 1
        expo += 1
        exposed(x, pop, expo, infec, reco)
    else:
        print("{} is NOT exposed!".format(str(x)))
        susceptible(x, pop, expo, infec, reco)

def exposed(x, pop, expo, infec, reco):
    tr = 0.3
    if decision(tr):
        print("{} is infected!".format(str(x)))
        expo -= 1
        infec += 1
        infected(x, pop, expo, infec, reco)
    else:
        print("{} is NOT infected!".format(str(x)))
        exposed(x, pop, expo, infec, reco)

def infected(x, pop, expo, infec, reco):
    tr = 0.3
    if decision(tr):
        print("{} is recovered!".format(str(x)))
        infec -= 1
        reco += 1
        recovered(x, pop, expo, infec, reco)
    else:
        print("{} is NOT exposed!".format(str(x)))
        infected(x, pop, expo, infec, reco)

def recovered(x, pop, expo, infec, reco):
    print("{} is recovered!".format(str(x)))

def main(x):
    pop = 1000
    expo = 0
    infec = 0
    reco = 0

    print("Current pop: ", pop)
    print(expo, infec, reco)
    for i in range(pop):
        susceptible(i, pop, expo, infec, reco)
        time.sleep(0.01)
    print(expo, infec, reco)


if __name__ == "__main__":
    main(123)