import numpy as np
import matplotlib.pyplot as plt


class ChaosGame:
    def __init__(self, n:int, r=1/2):

        '''
        Parameters
        ----------
        n : number of corners
        r : travel distance from last point

        Raises
        ------
        ValueError if n and x has the wrong values

        Returns
        -------
        None.

        '''
        if n<3 or (0 >= r or r>=1):

            raise ValueError("to run this n>=3 and 0<r<1.")
        if type(n) != int:
            raise ValueError(f"Expected n to be of type 'int', got {type(n)}")

        self.r = r
        self.n = n

        self._generate_ngon()
        self.gradient = None

    def _generate_ngon(self):
        '''
        creates n-gon
        '''
        theta=2*np.pi
        corners=[]
        
        for i in range(self.n):
            corners.append(
                [np.sin((theta / self.n) * (i + 1)), np.cos((theta / self.n) * (i + 1))]
            )
        self.corners = corners

    def plot_ngon(self):
        '''
        plots n-gon
        '''
        plt.scatter(*zip(*self.corners))
        plt.axis("equal")
        plt.show()
        
    def _starting_point(self,itr):
        '''
        Parameters
        ----------
        itr : number of iterations
        
        Returns
        -------
        array of x- and y-cordinates
        '''
        points = []

        for i in range(itr):
            weights = np.random.random(self.n)
            weight_sum = sum(weights)
            norm_weights = weights / weight_sum
            matrix = (
                np.transpose(self.corners) * norm_weights
            )  # corners need to be transposed to facilitate proper matrix-vector multiplication
            lincomb = sum(
                np.transpose(matrix)
            )  # matrix needs to be transposed in order to get the correct sum
            points.append(lincomb)
        return np.array(points)
    
    def iterate(self,steps, discard=5):
        '''
        Parameters
        ----------
        steps : number of iterations
        discard : How many to discard

        makes points and rand_index variables to use
        '''
        x0=self._starting_point(1)
        itr=steps+5
        x=[x0[0]]
        rand_index=[]
        
        for i in range(itr-1):
            rand_index.append(np.random.randint(self.n))
            c_j = np.array(self.corners[rand_index[i]])
            current = self.r * x[i] + (1 - self.r) * c_j
            x.append(current)

        self.points = np.array(x[discard:])
        self.rand_index = np.array(rand_index[discard - 1 :])
        self.make_gradient()

    def make_gradient(self):
      """Makes gradient"""
      colors = self.rand_index
      gradient_color = [colors[0]]
      for i in range(len(colors) - 1):
          gradient_color.append((gradient_color[i] + colors[i + 1]) / 2)
      self.gradient = gradient_color

    def plot(self, color=False, cmap="rainbow"):
        '''
        Parameters
        ----------
        color : decides if there's color
        cmap : which colormap to use

        Makes plot but doesn't show it
        '''

        if color == True:
            plt.scatter(*zip(*self.points), s=0.2, c=self.gradient, cmap=cmap)
            plt.axis("equal")
        else:
            plt.scatter(*zip(*self.points), s=0.2, c="black")
            plt.axis("equal")

    def show(self, color=False, cmap='rainbow'):
        '''
        shows plot
        '''
        self.plot(color, cmap)
        plt.show()
        
    def savepng(self, outfile, color=False, cmap='rainbow'):
        '''
        saves plot
        '''
        self.plot(color,cmap)

        plt.savefig(outfile, dpi=300)
        plt.clf()


if __name__ == "__main__":
    n = [3, 4, 5, 5, 6]
    r = [1 / 2, 1 / 3, 1 / 3, 3 / 8, 1 / 3]

    for i in range(len(n)):
        Game1 = ChaosGame(n[i], r[i])
        Game1.iterate(10000)
        Game1.savepng(f"figures/chaos{i+1}.png", color=True)
