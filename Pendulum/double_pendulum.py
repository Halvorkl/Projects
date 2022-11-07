from dataclasses import dataclass
from ode import *
import numpy as np 

class DoublePendulum(ODEModel):
    def __init__(self, L1 = 1, L2 = 1, g = 9.81):
        self.L1 = L1
        self.L2 = L2
        self.g = g
    
    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        #theta1, omega1, theta2, omega2 = u 
        
        L1 = self.L1
        L2 = self.L2
        g = self.g
        delta_theta = u[2] - u[0]

        dtheta1_dt = u[1]
        dtheta2_dt = u[3]

        domega1_dt = ((L1 * (u[1]**2) * np.sin(delta_theta) * np.cos(delta_theta)) + (g * np.sin(u[2]) 
        * np.cos(delta_theta)) + (L2 * (u[3]**2) * np.sin(delta_theta)) - (2*g * np.sin(u[0])))/((2 * L1)
        - (L1*(np.cos(delta_theta)**2)))

        domega2_dt = (-(L2 * (u[3]**2) * np.sin(delta_theta) * np.cos(delta_theta)) + (2 * g * np.sin(u[0]) 
        * np.cos(delta_theta)) - (2*L1 * (u[1]**2) * np.sin(delta_theta)) - (2*g * np.sin(u[2])))/((2 * L2)
        - (L2*(np.cos(delta_theta)**2)))

        return np.array([dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt])

    @property 
    def num_states(self) -> int:
        return 4

@dataclass
class DoublePendulumResults:
    results: ODEResult
    pendulum: DoublePendulum

    @property
    def theta1(self):
        return self.results.solution[0]
    @property
    def omega1(self):
        return self.results.solution[1]
    @property
    def theta2(self):
        return self.results.solution[2]
    @property
    def omega2(self):
        return self.results.solution[3]
    @property
    def L1(self):
        return self.pendulum.L1
    @property
    def L2(self):
        return self.pendulum.L2
    @property
    def g(self):
        return self.pendulum.g
    @property
    def x1(self) -> np.ndarray:
        return self.pendulum.L1 * np.sin(self.theta1)
    @property
    def y1(self) -> np.ndarray:
        return -self.pendulum.L1 * np.cos(self.theta1) 
    @property
    def x2(self) -> np.ndarray:
        return self.x1+self.L2*np.sin(self.theta2)
    @property
    def y2(self) -> np.ndarray:
        return self.y1-self.L2*np.cos(self.theta2)

def solve_double_pendulum(u0: np.ndarray,T: float,dt: float = 0.01,pendulum: Optional[DoublePendulum] = None,)-> DoublePendulumResults:
    if pendulum==None:
        model=DoublePendulum()
    else:
        model=pendulum
    sol = solve_ode(model, u0, T, dt)
    return DoublePendulumResults(sol, model)

