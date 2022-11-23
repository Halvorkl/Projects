import numpy as np
import matplotlib.pyplot as plt
import chaos_game


class Variations:
    def __init__(self, x: float, y: float, name: str) -> None:
        """Constructor for Variations class

        Parameters
        ----------
        x : float
            x - coordinate
        y : float
            y - coordinate
        name : str
            name of variation
        """
        self.x = x
        self.y = y
        self.name = name

        self._func = getattr(Variations, self.name)

    def transform(self):
        """Transforms variation instance"""
        return self._func(self.x, self.y)

    @classmethod
    def from_chaos_game(cls, chaos_inst: chaos_game.ChaosGame, name: str):
        """Takes instance of chaos game and transforms it with given method"""
        points2 = chaos_inst.points
        xlist = []
        ylist = []
        for e in points2:
            xlist.append(e[0])
            ylist.append(e[1])

        x = np.array(xlist)
        y = np.array(ylist)

        return cls(x, y, name).transform()

    @staticmethod
    def linear(x, y):
        """Linear method"""
        return x, y

    @staticmethod
    def handkerchief(x, y):
        """handkerchief method"""
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        return r * np.sin(theta + r), r * np.cos(theta + r)

    @staticmethod
    def disc(x, y):
        """disc method"""
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        return (theta / np.pi) * np.sin(np.pi * r), (theta / np.pi) * np.cos(np.pi * r)

    @staticmethod
    def swirl(x, y):
        """swirl method"""
        r = np.sqrt(x**2 + y**2)
        return x * np.sin(r**2) - y * np.cos(r**2), x * np.cos(r**2) + y * np.sin(
            r**2
        )

    @staticmethod
    def sinusodial(x, y):
        """sinusodial method"""
        return np.sin(x), np.sin(y)

    @staticmethod
    def spherical(x, y):
        """spherical method"""
        r = np.sqrt(x**2 + y**2)
        return (1 / (r**2)) * x, (1 / (r**2)) * y


if __name__ == "__main__":
    N = 100

    coords = np.linspace(-1, 1, N)
    x, y = np.meshgrid(coords, coords)

    x_values = x.flatten()
    y_values = y.flatten()

    transformations = [
        "spherical",
        "swirl",
        "linear",
        "sinusodial",
        "handkerchief",
        "disc",
    ]
    variations = [
        Variations(x_values, y_values, version) for version in transformations
    ]
    fig, axs = plt.subplots(2, 1, figsize=(9, 9))

    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations[:2])):
        u, v = variation.transform()
        ax.scatter(u, -v, s=0.2, marker=".", color="green")
        ax.set_title(variation.name)
        ax.axis("off")

    plt.axis("equal")
    fig.savefig("figures/variations_4b.png")

    fig, axs = plt.subplots(3, 2, figsize=(9, 9))

    chaos_inst = chaos_game.ChaosGame(3)
    chaos_inst.iterate(100000)

    gradient = chaos_inst.gradient

    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
        chaos_coords2 = Variations.from_chaos_game(chaos_inst, variation.name)
        ax.scatter(
            chaos_coords2[0], chaos_coords2[1], s=0.2, c=gradient, cmap="rainbow"
        )
        ax.set_title(variation.name)
        ax.axis("off")
    fig.savefig(f"figures/variations_chaos.png")

    plt.axis("equal")

    plt.show()
