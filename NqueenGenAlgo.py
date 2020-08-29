import random as rand
import numpy as np

fitness = []
npair = []
pmax = []
board = []
child = []

cou = 0


def calNpair(list1):  # calculates number of attacking pairs and subtracts it from the total possible non attacking pair
    # npair.clear()
    s = 0
    a = []
    arr = [[0 for i in range(len(list1))] for j in range(len(list1))]

    for i in range(len(list1)):
        arr[list1[i]][i] = 1

    arr[list1[0]][0] = 0

    for i in arr:
        x = i.count(1)
        if x > 1:
            x = (x * (x - 1)) / 2
            s = s + x

    narr = np.array(arr)

    for i in range(-len(list1) + 1, len(list1)):
        a = narr.diagonal(i).tolist()
        x = a.count(1)
        if x > 1:
            x = (x * (x - 1)) / 2
            s = s + x

    for i in range(-len(list1) + 1, len(list1)):
        a = np.fliplr(narr).diagonal(i).tolist()
        x = a.count(1)
        if x > 1:
            x = (x * (x - 1)) / 2
            s = s + x
    if s == 0:
        print(" config is perfect at cycle " + str(cou))
        print(list1[1:])
        exit()

    else:
        x = len(list1) - 1
        y = int((x*(x-1))/2)
        npair.append(y - s)


def calFitness(list1):  # calculates ration of non attacking pair
    a = np.array(list1)

    sum1 = a.sum();
    for i in range(len(list1)):
        fitness.append(list1[i] / sum1)


def selection(list1):  # selects the best two config with highest fitness or most non attacking pair
    a = np.array(list1)
    a = np.flip(np.sort(a))
    a = a.tolist()

    for i in a:
        pmax.append(i)


def crossOver():  # swaps the last from queen location between best two config
    i = fitness.index(pmax[0])
    j = 0

    if pmax[0] == pmax[1]:
        j = fitness.index(pmax[1], i + 1)
    else:
        j = fitness.index(pmax[1])

    child.append(board[i])
    child.append(board[j])

    child[0][5:len(child[0])], child[1][5:len(child[0])] = child[1][5:len(child[0])], child[0][5:len(child[0])]


def mutation():  # changes random values
    for i in child:
        i[rand.randint(1, 8)] = rand.randint(1, 8)


def rselection():  # uses mutation values along with random selection to create new population set
    for row in range(0, 2):
        list2 = []
        for c in range(0, 9):
            v = rand.randint(1, 8)
            list2.append(v)
        list2[0] = 0
        child.append(list2)

    board.clear();

    for k in child:
        board.append(k)


for i in range(0, 4):  # start of code, creates random 2d list with 8 queens can modifie jay to suit any number of queen
    list1 = []
    for j in range(0, 9):
        n = rand.randint(1, 8)
        list1.append(n)
    list1[0] = 0
    board.append(list1)


print("set of boards")
for i in board:
    print(i)

c = 9  # int(input("give cycle number"))

while c != 0:  # runs on infinite loop till answer
    cou = cou + 1
    for j in board:
        calNpair(j)
    print("non attacking pair count")
    print(npair)
    calFitness(npair)
    print("fitness Value")
    print(fitness)
    selection(fitness)
    # print(pmax)
    crossOver()
    npair.clear()
    pmax.clear()
    fitness.clear()
    mutation()
    rselection()
    print("set of boards")
    for k in board:
        print(k)
    child.clear()

for j in board:
    print(j)
npair.clear()
for j in board:
    calNpair(j)
print(npair)
calFitness(npair)
print(fitness)
selection(fitness)
print(pmax)
