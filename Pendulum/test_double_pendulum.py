import pytest
from ode import *
from double_pendulum import *
import numpy as np
tol=1e-6

def test_derivatives_at_rest_is_zero(): 
    u0 = np.array([0,0,0,0])
    model = DoublePendulum()
    results = model(None, u0)

    assert all(results) == 0 

@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0),
        (0, 0.5, 3.386187037),
        (0.5, 0, -7.678514423),
        (0.5, 0.5, -4.703164534),
    ],
)
def test_domega1_dt(theta1, theta2, expected):
    model = DoublePendulum()
    t = 0
    y = (theta1, 0.25, theta2, 0.15)
    dtheta1_dt, domega1_dt, _, _ = model(t, y)
    assert np.isclose(dtheta1_dt, 0.25)
    assert np.isclose(domega1_dt, expected)


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0.0),
        (0, 0.5, -7.704787325),
        (0.5, 0, 6.768494455),
        (0.5, 0.5, 0.0),
    ],
)
def test_domega2_dt(theta1, theta2, expected):
    model = DoublePendulum()
    t = 0
    y = (theta1, 0.25, theta2, 0.15)
    _, _, dtheta2_dt, domega2_dt = model(t, y)
    assert np.isclose(dtheta2_dt, 0.15)
    assert np.isclose(domega2_dt, expected)

def test_solve_pendulum_ode_with_zero_ic(): 
    model = DoublePendulum()
    u0 = np.array([0,0,0,0])
    T = 10 
    dt = 0.01 
    sol = solve_ode(model, u0, T, dt) 

    for i in range(model.num_states):
        assert all(sol.solution[i]) == 0 

def test_solve_double_pendulum_function_zero_ic():
    u0=np.array([0,0,0,0])
    T=10
    sol=solve_double_pendulum(u0,T)
    assert all(sol.omega1)==0
    assert all(sol.omega2)==0
    assert all(sol.theta1)==0
    assert all(sol.theta2)==0
    assert all(sol.x1)==0
    assert all(sol.x2)==0
    assert abs(sol.L1-tol)<abs(all(sol.y1))<abs(sol.L1+tol)
    #assert abs(sol.L1+sol.L2-tol)<=abs(all(sol.y2))<=(sol.L1+sol.L2+tol)


