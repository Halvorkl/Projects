from ode import *
import numpy as np
from dataclasses import dataclass
from typing import Optional

class Pendulum(ODEModel):
    def __init__(self, m = 1, l = 1, g = 9.81):
        self.m = m
        self.l = l
        self.g = g 

    def __call__(self, t, u: np.ndarray):
       d_theta = u[1]
       d_omega = (-self.g/self.l)*np.sin(u[0]) 
       return np.array([d_theta, d_omega])

    @property
    def num_states(self):
        return 2

def exercise_2b():
    """solves pendulum"""

    model = Pendulum()
    u0 = np.array([np.pi/6, 0.35])
    T = 10.0 #time
    dt = 0.01 #time step 
    
    sol = solve_ode(model, u0, T, dt)
    plot_ode_solution(sol, ["theta", "omega"], "exercise_2b.png")

@dataclass
class PendulumResults:
    results: ODEResult
    pendulum: Pendulum

    @property
    def theta(self):
        return self.results.solution[0]
    @property
    def omega(self):
        return self.results.solution[1]
    @property
    def l(self):
        return self.pendulum.l
    @property
    def m(self):
        return self.pendulum.m
    @property
    def g(self):
        return self.pendulum.g
    @property
    def x(self) -> np.ndarray:
        return self.pendulum.l * np.sin(self.theta)
    @property
    def y(self) -> np.ndarray:
        return -self.pendulum.l * np.cos(self.theta) 

    @property
    def vy(self):
        return np.gradient(self.y, self.results.time)
    @property
    def vx(self):
        return np.gradient(self.x, self.results.time)
    @property
    def potential(self):
        return self.g*(self.y+self.l)
    @property
    def kinetic(self):
        return 1/2*(self.vx**2+self.vy**2)
    @property
    def total_enegry(self):
        return self.kinetic+self.potential
        


def solve_pendulum(
    u0: np.ndarray, T: float, dt: float = 0.01, pendulum: Optional[Pendulum] = None
) -> PendulumResults:
    """Solves pendulum ODE"""
    
    #if-else block for handling optional pendulum instance 
    if pendulum == None: 
        model = Pendulum()
    else: 
        model = pendulum

    #computes solution 
    sol = solve_ode(model, u0, T, dt)
    return PendulumResults(sol, model)
    
def plot_energy(results: PendulumResults, filename: Optional[str] = None) -> None:
    plt.plot(results.results.time,results.kinetic, label="kinetic")
    plt.plot(results.results.time,results.potential, label="potential")
    plt.plot(results.results.time,results.total_enegry, label="Total energy")
    plt.legend()
    if filename==None:
        plt.show()
    else:
        plt.savefig(filename)
        plt.clf()

def exercise_2g():
    u0=np.array([np.pi/6,0.35])
    pen=solve_pendulum(u0,10, dt=0.01)
    plot_energy(pen,filename="energy_single.png")

class DampenedPendulum(Pendulum):
    def __init__(self,B=0, m=1, l=1, g=9.81):
        super().__init__(m, l, g)
        self.B=B
    def __call__(self, t, u: np.ndarray):
        return super().__call__(t, u)-self.B*u[0]

def exercise_2h():
    u0=np.array([np.pi/6,0.35])
    pen=solve_pendulum(u0,10,dt=0.01,pendulum=DampenedPendulum(B=1))
    plot_energy(pen,"energy_damped.png")
        
if __name__ == "__main__":
    exercise_2b()
    exercise_2g()#den totale energien holder seg konstant
    exercise_2h()#energien faller i henhold til funksjonen