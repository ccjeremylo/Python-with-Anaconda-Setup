import numpy as np


def adding_numbers(a: float, b: float) -> float:
    """
    Adding a and b
    """
    return a + b


def combine_strings(first_name: str, last_name: str, age: int) -> str:
    """
    Return a string that introduces the person
    """
    assert age >= 0
    greeting = f"Hi, My name is {first_name}. My full name is {first_name} {last_name}. I am {age} years old."
    return greeting


def print_n_times(msg: str, n: int) -> None:
    """
    Printing the msg n times
    """
    assert n >= 0
    for i in np.arange(n):
        print(f"{i}: " + msg + f", i**2 = {i**2}")
