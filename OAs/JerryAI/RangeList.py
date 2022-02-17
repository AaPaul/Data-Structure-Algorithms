from typing import List

class RangeList:
    def __init__(self) -> None:
        """
        self.res: the list of final result including the range elements
        self.res_range_list: the list includes the element in self.res. In this list, every element is expanded.

        For example:
        self.res = [[1, 5]], which represents that there is one range element which is [1, 5)
        """
        self.res = list()
    def formatting(self, init_range: List[int]) -> List[int]:
        """
        To initialize the list with elments based on the required range
        
        Args:
        init_range: A list with 2 elements which defines the range. The first element and the second one represent that 
        the start and the end of the range.

        Return:
        rList: A list inlcludes the elements from init_range[0] to init_range[1] (not included)        
        """
        rList = [i for i in range(init_range[0], init_range[1])]
        return rList

    def add(self, init_range:List[int]) -> None:
        """
        Adds a range to the list
        @param {Array<number>} range - Array of two integers that specify
        beginning and end of range.

        Args:
        init_range: A list with 2 elements which defines the range. The first element and the second one represent that 
        the start and the end of the range.

        Returns: No return. Only add the new element into the res list
        """
        # represent whether the init_range is added or not
        flag = False
        ans = []
        if not self.res:
            self.res.append(init_range)
            return
        for left, right in self.res:
            if left > init_range[1]:
                if not flag:
                    ans.append(init_range)
                    flag = True
                ans.append([left, right])
            elif right < init_range[0]:
                ans.append([left, right])
            else:
                init_range[0] = min(left, init_range[0])
                init_range[1] = max(right, init_range[1])

        if not flag:
            ans.append(init_range)
        self.res = ans

    
    def remove(self, init_range:List[int]) -> None:
        """
        Removes a range from the list
        @param {Array<number>} range - Array of two integers that specify
        beginning and end of range.

        Args:
        init_range: A list with 2 elements which defines the range. The first element and the second one represent that 
        the start and the end of the range.

        Return: No return. Only remove the element from the res list
        """
        # represent whether the init_range is added or not
        ans = []
        for left, right in self.res:
            if left >= init_range[1] or right <= init_range[0]:
                ans.append([left, right])
            else:
                if left < init_range[0]:
                    ans.append([left, init_range[0]])
                if right > init_range[1]:
                    ans.append([init_range[1], right])

        self.res = ans

    def print(self) -> None:
        """
        Prints out the list of ranges in the range list
        """
        print(self.res)
    
    def printAllElements(self) -> None:
        """
        Print out expanded version of the list.
        """
        ans = []
        for rl in self.res:
            temp = []
            for item in range(rl[0], rl[1]):
                temp.append(item)
            ans.append(temp)
        print("RangeList {0}:\n{1}\n".format(self.res, ans))

def checkList() -> None:

    """
    To check if the function works well.
    
    print out the list with interval elements
    """
    rl = RangeList()

    rl.add([1, 5]) 
    rl.print() 
    # // Should display: [1, 5)

    rl.add([10, 20]) 
    rl.print() 
    # // Should display: [1, 5) [10, 20)


    rl.add([20, 20]) 
    rl.print() 
    # // Should display: [1, 5) [10, 20)

    rl.add([20, 21]) 
    rl.print() 
    # // Should display: [1, 5) [10, 21)

    rl.add([2, 4]) 
    rl.print() 
    # // Should display: [1, 5) [10, 21)

    rl.add([3, 8]) 
    rl.print() 
    # // Should display: [1, 8) [10, 21)

    rl.remove([10, 10]) 
    rl.print() 
    # // Should display: [1, 8) [10, 21)

    rl.remove([10, 11]) 
    rl.print() 
    # // Should display: [1, 8) [11, 21)

    rl.remove([15, 17]) 
    rl.print() 
    # // Should display: [1, 8) [11, 15) [17, 21)

    rl.remove([3, 19]) 
    rl.print() 
    # // Should display: [1, 3) [19, 21)

def checkListDetails() -> None:
    """
    To flatten the intervals.
    print out the detail of the list.
    """
    rl_new = RangeList()
    rl_new.add([1, 5]) 
    rl_new.printAllElements()
    # // Should display: [1, 5)

    rl_new.add([10, 20]) 
    rl_new.printAllElements() 
    # // Should display: [1, 5) [10, 20)


    rl_new.add([20, 20]) 
    rl_new.printAllElements() 
    # // Should display: [1, 5) [10, 20)

    rl_new.add([20, 21]) 
    rl_new.printAllElements() 
    # // Should display: [1, 5) [10, 21)

    rl_new.add([2, 4]) 
    rl_new.printAllElements() 
    # // Should display: [1, 5) [10, 21)

    rl_new.add([3, 8]) 
    rl_new.printAllElements() 
    # // Should display: [1, 8) [10, 21)

    rl_new.remove([10, 10]) 
    rl_new.printAllElements() 
    # // Should display: [1, 8) [10, 21)

    rl_new.remove([10, 11]) 
    rl_new.printAllElements() 
    # // Should display: [1, 8) [11, 21)

    rl_new.remove([15, 17]) 
    rl_new.printAllElements() 
    # // Should display: [1, 8) [11, 15) [17, 21)

    rl_new.remove([3, 19]) 
    rl_new.printAllElements() 
    # // Should display: [1, 3) [19, 21)


if __name__ == "__main__":
    # The function named checkList is to run the test cases from the file
    checkList()
    
    # The function named checkListDetails to print out the flatten version of invercal list.
    # checkListDetails()
