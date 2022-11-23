from array import array
import numpy as np
import matplotlib.pyplot as plt

c0 = np.array([0, 0])
c1 = np.array([1, 0])
c2 = np.array([0.5, np.sqrt(3) / 2])

tri_corners = np.array([c0, c1, c2])


def find_weights(corners: np.array) -> np.array:
    """Finds weights of the corners of a n-gon

    Parameters
    ----------
    n : np.array
        nested numpy array containing x and y coordinates of corners in n-gon

    Returns
    -------
    np.array
        array containing weights
    """
    n = len(corners)

    weights = np.random.random(n)

    weight_sum = sum(weights)

    norm_weights = weights / weight_sum
    return norm_weights


def compute_points(n: int, corners: np.array) -> np.array:
    """computes n number of points from a linear combination of corners and associated weights

    Parameters
    ----------
    n : int
        number of points to be computed
    corners : np.array
        nested numpy array containing x and y coordinates of corners in n-gon


    Returns
    -------
    np.array
        nested numpy array contaning x and y coordinates of n points point
    """
    points = []
    for i in range(n):
        matrix = np.transpose(corners) * find_weights(
            corners
        )  # corners need to be transposed to facilitate proper matrix-vector multiplication
        lincomb = sum(
            np.transpose(matrix)
        )  # matrix needs to be transposed in order to get the correct sum
        points.append(lincomb)

    return np.array(points)


def half_corner_point(itr: int, corners: np.array) -> np.array:
    """Creates random points between random corners of n-gon

    Parameters
    ----------
    itr : int
        number of iterations, ie number of points
    corners : np.array
        nested numpy array containing x and y coordinates of corners in n-gon

    Returns
    -------
    np.array
        nested numpy array containing x and y coordinates of points within n-gon
    """
    n_gon_dim = len(corners)

    n = itr + 5
    x0 = compute_points(1, corners)[0]

    points = [x0]
    rand_index=[]
    for i in range(n - 1):
        rand_index.append(np.random.randint(n_gon_dim))
        var = (points[i] + corners[rand_index[i]]) / 2
        points.append(var)
    return np.array(points[5:]), np.array(rand_index[4:])


def color_half_corner_point(itr: int, corners: np.array) -> tuple:
    """Creates random points between random corners of n-gon. Now with fancy colors!

    Parameters
    ----------
    itr : int
        number of iterations, ie number of points
    corners : np.array
        nested numpy array containing x and y coordinates of corners in n-gon
    colors : dict
        list containing colors corresponding to corners. The indeces in colors need to
        correspond to the indeces of corners as they are listed in the corner array

    Returns
    -------
    tuple
        tuple containing a nested numpy array containing x and y coordinates of points within n-gon
        with corresponding colors
    """
    triangle=half_corner_point(itr, corners)
    rand_index=triangle[1]
    points=triangle[0]
    color_map = []
    colors = ["red", "green", "blue"]
    for i in range(itr):
        color_map.append(colors[rand_index[i]])
    return np.array(points), np.array(color_map)

def rgb_corner_point(itr: int, corners: np.array) -> tuple:
    '''
    Parameters
    ----------
    itr : number of iterations
    corners : cordinates for corners

    Returns
    -------
    a tuple of x- and y- cordinates and a tuople og colors

    '''
    triangle=half_corner_point(itr, corners)
    rand_index=triangle[1]
    points=triangle[0]
    corner_colors = np.array([[1,0,0],[0,1,0],[0,0,1]])
    colors=[[0,0,0]]
    for i in range(itr):
        colors.append((colors[i]+corner_colors[rand_index[i]])/2)
    
    return np.array(points), np.array(colors[1:])

if __name__ == "__main__":
    results = rgb_corner_point(10000, tri_corners)
    coords = results[0]
    colors = results[1]

    plt.scatter(*zip(*coords), s=0.1, color=colors)

    plt.axis("equal")
    plt.axis("off")
    plt.show()
