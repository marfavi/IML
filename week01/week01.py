# Import necessary libraries 
import numpy as np
import matplotlib.pyplot as plt

def task_01():
    def length(v):
        sum = 0
        for v_i in v:
            sum += v_i**2
        return np.sqrt(sum)

    va = [2, 2]
    vb = [3, 4]

    print('a', length(va))
    print('b', length(vb))
    assert length(va) == 8**0.5
    assert length(vb) == 5


def task_02():
    def length(v):
        return np.sqrt(sum([v_i**2 for v_i in v]))

    va = [2, 2]
    vb = [3, 4]

    print('a', length(va))
    print('b', length(vb))
    assert length(va) == 8**0.5
    assert length(vb) == 5


def task_03():
    va = [2, 2]
    vb = [3, 4]

    def dot(a, b):
        return sum([a_i * b_i for (a_i, b_i) in zip(a,b)])

    # Tests
    assert dot(va, vb) == 14


def task_04():
    A = np.array([
        [1, 2, 3],
        [3, 4, 9],
        [5, 7, 3]
    ])

    ur = A[:2,1:]
    row = A[1]
    col = A[:, 0]

    print('upper right\n', ur)
    print('row', row)
    print('column', col)

    # Tests
    assert np.all(ur == np.array([[2, 3], [4, 9]]))
    assert np.all(row == np.array([3, 4, 9]))
    assert np.all(col == np.array([1, 3, 5]))

# task_01()
# task_02()
# task_03()
task_04()
