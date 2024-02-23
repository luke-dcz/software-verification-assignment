from hypothesis import given, strategies as st
from hypothesis.stateful import rule, precondition, RuleBasedStateMachine, Bundle

# main insertion sort method
def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1

		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	return arr

# method to check if a list is sorted
def isSorted(list):
	flag = 0
	i = 1
	while i < len(list):
		if(list[i] < list[i - 1]):
			flag = 1
		i += 1
	return not flag

# method to push a value to a list
def listPush(list, value):
	list.append(value)

# method to merge two lists together
def mergeLists(list1, list2):
	result = list(list1)
	for v in list2:
		listPush(result, v)
	return result

# basic unit test with given to check if a list is sorted after using insertion sort
@given(st.lists(st.integers()))
def test_insertionSort_sorts_list(list):
	assert isSorted(insertionSort(list)) == True

# Basic Insertion Sort State Machine. It makes use of the functions defined above, and the rule and precondition methods.
class InsertionMachine(RuleBasedStateMachine):
	def __init__(self):
		super(InsertionMachine, self).__init__()
		self.list = []
	
	@rule(value=st.integers())
	def push(self, value):
		listPush(self.list, value)
	
	@rule()
	@precondition(lambda self: self.list)
	def sort(self):
		result = insertionSort(self.list)
		assert isSorted(result) == True
	
TestInsertionMachine = InsertionMachine.TestCase
