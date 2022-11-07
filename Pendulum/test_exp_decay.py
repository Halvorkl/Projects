from pickletools import pyset
import pytest
import numpy as np
import exp_decay
from ode import InvalidInitialConditionError, ODEModel, solve_ode, ODEResult, plot_ode_solution
from scipy.integrate import solve_ivp
from pathlib import Path


def test_a_is_neg_raises_valueerror():
    with pytest.raises(ValueError):
        exp_decay.ExponentialDecay(-1)  

def test_returns_correct_value():
    model_test = exp_decay.ExponentialDecay(0.4)
    u = np.array([3.2])
    t = 0.0
    tol = 1e-6
    expected_value = -1.28
    computed_value = model_test(t, u)
    assert abs(expected_value - computed_value) < tol

def test_negative_decay_raises_ValueError():
    with pytest.raises(ValueError):
        model = exp_decay.ExponentialDecay(0.4)
        model.a = -1.0

def test_NotImplementedError():
        model = exp_decay.ExponentialDecay(0.4)
        assert model.num_states == 1
            
def test_solve_with_different_number_of_initial_states(): 
    with pytest.raises(InvalidInitialConditionError): 
        model = exp_decay.ExponentialDecay(0.4)
        solve_ode(model, np.array([1,2]), 10, 0.01)

@pytest.mark.parametrize("arg_a, arg_u0, arg_T, arg_dt", [(0.4, 0, 10, 1), (0.1, 2, 5, 0.1), (1, 9, 100, 2)])
def test_solve_time(arg_a, arg_u0, arg_T, arg_dt):
    model = exp_decay.ExponentialDecay(arg_a)
    u0 = np.array([arg_u0])
    T = arg_T 
    dt = arg_dt 
    sol_time = solve_ode(model, u0, T, dt).time
    assert sol_time[0] == 0 
    assert sol_time[-1] == T
    assert sol_time[1] - sol_time[0] == dt #seems a bit wonky to have three assert statements in one test

@pytest.mark.parametrize("arg_a, arg_u0, arg_T, arg_dt", [(0.4, 1, 10, 1), (0.1, 2, 5, 0.1), (1, 9, 100, 0.01)])
def test_solve_solution(arg_a, arg_u0, arg_T, arg_dt):
    model = exp_decay.ExponentialDecay(arg_a)
    u = np.array([arg_u0])
    t = np.arange(0, arg_T + arg_dt, arg_dt)
    y = solve_ode(model, u, arg_T, arg_dt).solution
    y_exact=np.array(arg_u0 * np.exp(-arg_a * t))
    relative_error = np.linalg.norm(y - y_exact) / np.linalg.norm(y_exact)
    assert relative_error < 0.01

def test_ODEResults():
    results = ODEResult(time=np.array([0, 1, 2]), solution=np.zeros((2, 3)))
    assert results.num_timepoints==3
    assert results.num_states==2

def test_plot_ode_solution_saves_file():
    model = exp_decay.ExponentialDecay(0.4)
    result = solve_ode(model, u0=np.array([4.0]), T=10.0, dt=0.01)
    plot_ode_solution(results=result, state_labels=["u"],
    filename="test_plot.png")

def test_function_that_creates_a_file():

    # Check if the file already exists and delete if necessary
    filename = Path("test_plot.png")
    if filename.is_file():
        filename.unlink()

    # Call the function we are testing
    test_plot_ode_solution_saves_file()

    # Check that the file has now been created, then delete it
    assert filename.is_file()
    filename.unlink()