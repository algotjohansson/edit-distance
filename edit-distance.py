import numpy as np


def edit_distance(s1, s2):
    table = np.zeros((len(s1)+1, len(s2)+1))
    table[0] = np.arange(0, len(s2)+1)
    table[:, 0] = np.arange(0, len(s1)+1)

    for i in range(len(s1)):
        for j in range(len(s2)):
            if(s1[i] == s2[j]):
                table[i+1, j+1] = table[i, j]
            else:
                table[i+1, j+1] = 1 + min([
                    table[i, j+1],
                    table[i+1, j],
                    table[i, j]])

    return table[-1, -1]


assert(edit_distance("benyam", "ephrem") == 5)
assert(edit_distance("book", "back") == 2)
