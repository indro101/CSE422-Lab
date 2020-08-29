import numpy as np

list1 = np.array(
         [[-2,  5,  3,  2],
          [ 9, -6,  5,  1],
          [ 3,  2,  7,  3],
          [-1,  8, -4,  8]])


for i in range(-len(list1)+1, len(list1)):
    a = list1.diagonal(i).tolist()
    #x = a.count(1)
    print(i)
    print(a)

print("2nd diagonal")

for i in range(-len(list1)+1, len(list1)):
    a = np.fliplr(list1).diagonal(i).tolist()
    #x = a.count(1)
    print(i)
    print(a)