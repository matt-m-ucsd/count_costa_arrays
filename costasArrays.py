import itertools
import time


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __init__(self, x, y):
        self.p1 = Point(0, 0)
        self.p2 = Point(x, y)


class MatVector:
    def __init__(self, index, n):
        self.elements = []
        for i in range(n):
            if i == index:
                self.elements.append(1)
            else:
                self.elements.append(0)
        self.mark = index


class Matrix:
    def __init__(self, mat_vector_list, n):
        self.elements = [[0 for x in range(n)] for y in range(n)]
        self.marked = []

        for i in range(n):
            for j in range(n):
                if mat_vector_list[i].elements[j] == 1:
                    self.marked.append(Point(i, j))
                self.elements[j][i] = mat_vector_list[i].elements[j]


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def calc_d_v(p1, p2):
    v = Vector(p2.x - p1.x, p2.y - p1.y)
    return v


def is_costa(matrix):
    v_arr = []
    for i in range(len(matrix.marked)):
        for j in range(i + 1, len(matrix.marked)):
            d_v = calc_d_v(matrix.marked[i], matrix.marked[j])
            for a in range(len(v_arr)):
                if d_v.p1.x == v_arr[a].p1.x and d_v.p1.y == v_arr[a].p1.y:
                    if d_v.p2.x == v_arr[a].p2.x and d_v.p2.y == v_arr[a].p2.y:
                        return False
            else:
                v_arr.append(d_v)
    return True


def main():
    start = time.time()
    n = int(input("Order: "))
    count = 0
    mat_vector_list = []

    for i in range(n):
        mat_vector_list.append(MatVector(i, n))

    perm_list = list(itertools.permutations(mat_vector_list))

    for i in range(factorial(n)):
        if is_costa(Matrix(perm_list[i], n)):
            count += 1
    print(n, " -> ", count)
    end = time.time()
    print(end - start, "seconds")


if __name__ == "__main__":
    main()