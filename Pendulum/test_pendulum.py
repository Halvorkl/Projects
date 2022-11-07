import pytest
import numpy as np
from pendulum import *

tol = 1e-6

def test_pendulum_solution_matches_computed_values():
    model = Pendulum(l = 1.42)
    u = np.array([np.pi/6, 0.35])
    results = model(None, u)
    computed_d_theta = 0.35
    computed_d_omega = -981/284
    assert abs(results[0] - computed_d_theta) < tol and abs(results[1] - computed_d_omega) < tol

def test_pendulum_derivatives_are_zero_at_rest():
    model = Pendulum(l = 1.42)
    u = np.array([0, 0])
    results = model(None, u)
    computed_d_theta = 0
    computed_d_omega = 0 
    assert abs(results[0] - computed_d_theta) < tol and abs(results[1] - computed_d_omega) < tol

def test_solve_pendulum_ode_with_zero_ic():
    model = Pendulum()
    u0 = np.array([0, 0])
    T = 10.0 #time
    dt = 0.01 #time step 
    
    sol = solve_ode(model, u0, T, dt)
    assert all(sol.solution[0]) == 0.0 and all(sol.solution[1]) == 0 

def test_solve_pendulum_function_zero_ic():
    u0 = np.array([0,0])
    T = 10.0 
    dt = 0.01

    sol = solve_pendulum(u0, T, dt)

    print(sol.y, sol.l)

    assert all(sol.x) == 0 
    assert sol.l - tol <= all(sol.y) <= sol.l + tol  
    assert all(sol.theta) == 0 
    assert all(sol.omega) == 0 
