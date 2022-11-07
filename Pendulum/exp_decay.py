import numpy as np
from ode import ODEModel 
from scipy.integrate import solve_ivp

class ExponentialDecay(ODEModel):
    def __init__(self, a):
        self.a = a
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self,a):
        if a < 0: 
            raise ValueError
        self._a=a
    @property
    def num_states(self):
        return 1

    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        return -self.a * u

def solve_exponential_decay(d,t,dt,u0):
    T = np.arange(0,t, dt)
    model = ExponentialDecay(d)
    sol = solve_ivp(model, [0,t],u0,t_eval = T) 
    return sol

if __name__ == "__main__":
    print(solve_exponential_decay(0.4, 10, 0.01, [0.1]))
