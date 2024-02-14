from hypothesis import given, strategies as st

def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1

		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	return arr

def isSorted(list):
	flag = 0
	i = 1
	while i < len(list):
		if(list[i] < list[i - 1]):
			flag = 1
		i += 1
	return not flag

@given(st.lists(st.integers()))
def test_insertionSort_sorts_list(list):
	assert isSorted(insertionSort(list)) == True