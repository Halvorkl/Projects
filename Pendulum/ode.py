import numpy as np
from scipy.integrate import solve_ivp
from typing import Optional, List
from typing import NamedTuple
import matplotlib.pyplot as plt

class ODEModel():
    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        raise NotImplementedError
    @property
    def num_states(self) -> int:
        raise NotImplementedError

class ODEResult(NamedTuple):
    time: np.ndarray
    solution: np.ndarray

    @property
    def num_timepoints(self):
        try:
            type(self.solution.shape[1]) #this shows if the array is 2 dimentional, 1 state solutions will return one-dimentional arrays
            time_=self.solution.shape[1]
        except:
            time_=self.solution.shape[0]
        return time_

    @property
    def num_states(self):
        try:
            type(self.solution.shape[1])
            _solution=self.solution.shape[0]
        except:
            _solution=1#has to be one if the solution is one-dimentional
        return _solution

class InvalidInitialConditionError(RuntimeError):
    pass

def solve_ode(model: ODEModel, u0: np.ndarray, T: float, dt: float,) -> ODEResult:
    """Solves ODE"""

    if len(u0) != model.num_states: 
        raise InvalidInitialConditionError(f"Expected {model.num_states} initial conditions, got {len(u0)}")
    x_values = np.arange(0,T + dt, dt)

    sol = solve_ivp(model, [0,T], u0, t_eval = x_values) 
    return ODEResult(sol.t, sol.y)

def plot_ode_solution(
    results: ODEResult,
    state_labels: Optional[List[str]] = None,
    filename: Optional[str] = None,
) -> None:
    """Plots ODE solution"""

    for i in range(results.num_states):
        if state_labels!=None:
         plt.plot(results.time, results.solution[i], label = f"{state_labels[i]}")
           #Has to have state_lables for every state
        else:
            plt.title(f"state {i+1}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    if filename==None:
        plt.show()
    else:
        plt.savefig(filename)
        plt.clf()


if __name__ == "__main__":
    pass
