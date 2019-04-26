from src.Sorting import SortingAlgorithms

class TestSortingAlgorithms(object):
    unsortedList = [3, 1, 6, 4, 2, 5]
    unsortedMultipleList = [3, 1, 6, 4, 3, 2, 5]
    expectedResult = [1, 2, 3, 4, 5, 6]
    emptyList = []

    def test_bubbleSort(self):
        assert SortingAlgorithms.bubbleSort(self, self.unsortedList) == self.expectedResult

    def test_bubbleSort_EmptyList(self):
        assert SortingAlgorithms.bubbleSort(self, self.emptyList) == []

    def test_quickSort(self):
        assert SortingAlgorithms.quickSort(self, self.unsortedList) == self.expectedResult

    def test_quickSort_EmptyList(self):
        assert SortingAlgorithms.quickSort(self, self.emptyList) == []

    def test_quickSort_Multiples(self):
        assert SortingAlgorithms.quickSort(self, self.unsortedMultipleList) == [1, 2, 3, 3, 4, 5, 6]
