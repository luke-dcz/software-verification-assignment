import threading
import time
import random
from hypothesis import given
from hypothesis.strategies import integers

contested_variable = True
function_1_sleep_time = random.randint(0, 1)
function_2_sleep_time = random.randint(0, 1)

def function_1(input_number):
    global contested_variable
    time.sleep(function_1_sleep_time)
    if contested_variable == True:
        contested_variable = False
        return 10 * input_number
    else:
        return input_number

def function_2(input_number):
    global contested_variable
    time.sleep(function_2_sleep_time)
    if contested_variable == False:
        contested_variable = True
        return 20 * input_number
    else:
        return input_number

@given(integers())
def test_function_1 (i):
    assert function_1(i) == i * 10

@given(integers())
def test_function_2 (i):
    assert function_2(i) == i * 20
    