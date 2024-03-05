import threading
import time
import random
from hypothesis import given
from hypothesis.strategies import integers

contested_variable = True
sleep_time = random.randint(0, 1)
thread_1_output = 0
thread_2_output = 0


def function_1(input_number):
    global contested_variable
    global thread_1_output
    time.sleep(0.5)
    if contested_variable == True:
        contested_variable = False
        thread_1_output = 10 * input_number

def function_2(input_number):
    global contested_variable
    global thread_2_output
    time.sleep(sleep_time)
    if contested_variable == False:
        contested_variable = True
        thread_2_output = 20 * input_number

@given(integers())
def test_function_1 (i):
    global contested_variable
    global thread_1_output
    global thread_2_output
    threading.Thread(target=function_1, args=(i,)).start()
    threading.Thread(target=function_2, args=(i,)).start()
    assert thread_1_output == i * 10
    assert thread_2_output == i * 20


# gives error due to inconsisent behaviour however this is not ideal if this is the behaviour you want. 
# you cannot test what happens if one thread finishes before the other if you cannot control run times.
# even if you identify which thread ends first you get an error.
    