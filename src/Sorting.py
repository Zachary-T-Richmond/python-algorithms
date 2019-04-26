class SortingAlgorithms:

    def bubbleSort(self, arr):

        """
        Bubble Sort is an algorithm to sort a list of integers byt swapping adjacent elements
        if they are not in the correct order. Example: [3, 1] -> [1, 3].

        BigO Notation
        -------------
        N**2

        Parameters
        ----------
        arr: unsorted list of ints

        Returns
        -------
        arr: sorted list of ints
        """

        length = len(arr)
        if (length is 0):
            return arr

        for i in range(length - 1):
            for j in range(length - i - 1):

                if (arr[j] > arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def quickSort(self, arr):

        """
        Quick Sort is an alogrithm for sorting an integer list. This algorithm selects whatever number is at position 0.
        Once the pivot has been selected, every other number in the list is compared to the pivot. If the number
        is greater than, then it is put into a greater than list. If the number is less than, then it is put into
        a less than list. If there are multiples of the pivot, then the multiples are placed in the less than list.
        After the first round of sorting, recursion is used to sort the greater and lesser lists following the above
        steps until the entire list is sorted.

        BigO Notation
        -------------
        Depends on the pivot choice
        Average: N*logN
        Max: N**2

        Parameters
        ----------
        arr: unsorted list of ints

        Returns
        -------
        arr: sorted list of ints
        """

        length = len(arr)

        if(length is 0):
            return []

        pivotInt = arr[0]
        greaterThanPivot = []
        lessThanPivot = []

        for i in range(1, length):
            if(arr[i] > pivotInt):
                greaterThanPivot.append(arr[i])
            else:
                lessThanPivot.append(arr[i])

        return SortingAlgorithms.quickSort(self, lessThanPivot) + [pivotInt] + SortingAlgorithms.quickSort(self, greaterThanPivot)


