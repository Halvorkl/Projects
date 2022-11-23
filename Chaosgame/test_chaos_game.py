from chaos_game import *
import pytest

def test_constructor_throws_error_for_bogus_n_values():
    '''
    tests that the constructor trows error if n-values are outside our parameters
    '''
    n_Val = [-1,0,1,2,2.3]
    for e in n_Val:
        with pytest.raises(ValueError):
                ChaosGame(e) 

def test_constructor_throws_error_for_bogus_r_values():
    '''
    tests that the constructor trows error if r-values are outside our parameters
    '''
    r_Val = [-1,0,1,2]
    for e in r_Val:
        with pytest.raises(ValueError):
                ChaosGame(3, e) 

def test_generate_n_gon_creates_correct_number_of_corners():
    '''
    test that the "generate_n_gon" method genereates the correct n-gon
    '''
    n = 6 #expected corners
    test_game = ChaosGame(n)
    computed_corners = len(test_game.corners) 
    msg = f"Expected n-gon to have {n} corners, got {computed_corners}"

    assert computed_corners == n, msg

def test_iterate_returns_expected_no_of_points():
    '''
    tests that the iterate method return the correct number og points
    '''
    n = 1000 #expected points
    test_game = ChaosGame(5)
    test_game.iterate(n)
    computed_points = len(test_game.points) 
    msg = f"Expected n-gon to have {n} poitns, got {computed_points}"

    assert computed_points == n, msg