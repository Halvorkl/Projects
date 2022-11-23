import numpy as np
import matplotlib.pyplot as plt


class AffineTransform:
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        abcd_matrix = np.array([[self.a, self.b], [self.c, self.d]])
        xy_vector = np.array([x, y])
        ef_vector = np.array([self.e, self.f])
        self.f = np.dot(abcd_matrix, xy_vector) + ef_vector
        return self.f


import numpy as np
import matplotlib.pyplot as plt


class AffineTransform:
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        abcd_matrix = np.array([[self.a, self.b], [self.c, self.d]])
        xy_vector = np.array([x, y])
        ef_vector = np.array([self.e, self.f])
        self.val = np.dot(abcd_matrix, xy_vector) + ef_vector
        return self.val


def probability(p_c, functions):
    r = np.random.random()
    prob = 0
    for j, p in enumerate(p_c):
        prob += p
        if r < prob:
            return functions[j]


def itarate(steps, p_c, functions):
    x = [[0, 0]]
    for i in range(steps):
        current = probability(p_c, functions)
        x.append(current(x[i][0], x[i][1]))
    return x


functions = [
    AffineTransform(d=0.16),
    AffineTransform(a=0.85, b=0.04, c=-0.04, d=0.85, f=1.6),
    AffineTransform(a=0.20, b=-0.26, c=0.23, d=0.22, f=1.6),
    AffineTransform(a=-0.15, b=0.28, c=0.26, d=0.24, f=0.44),
]

p_c = [0.01, 0.85, 0.07, 0.07]


if __name__ == "__main__":
    fern = itarate(50000, p_c, functions)
    plt.scatter(*zip(*fern), s=0.4, c="forestgreen")
    plt.axis("equal")
    plt.savefig("barnsley_fern.png", dpi=300)
