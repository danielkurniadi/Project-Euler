import math

"""
Work out the first ten digits of the sum of the following N-50-digit numbers.

Input Format:
    First line contains input for number N
    Second to next N lines contain a 50 digit number each.

Output Format:
    Find the sum of those N numbers and give the first 10 digit of the sum !

Example:
    - Sample input:
    ``` 
        5
        37107287533902102798797998220837590246510135740250
        46376937677490009712648124896970078050417018260538
        74324986199524741059474233309513058123726617309629
        91942213363574161572522430563301811072406154908250
        23067588207539346171171980310421047513778063246676
    ```
    - Sample output:
    ```
        // sum of those 5 numbers is 272819012982030361314614767301043585006837989465343, 
        // hence the first 10 digit is
        2728190129 
        100000000000
    ```
"""

class BaseSolution():
    """Solution base class"""

    def __init__(self):
        print("initialise %s", self.__class__.__name__)

    def solve(self):
        print("solving...")

class BruteSolution(BaseSolution):
    """ Brute force solution class """ 

    def solve(self, is_io_input=True, numbers=None):
        """ 
            1. Let python do the thing
            2. Enjoy!

            Args:
                is_io_input (bool): if true, you must manually type in the inputs as above from the standard I/O python shell
                numbers (list): pass a list of 50 digits numbers if you have. will only calculated if is_io_input is False. 
        """
        if is_io_input:
            return self.solve_shortcut()
        elif len(numbers)>0:
            result = sum(numbers)//10**40
            while(result >= 10**10):
                result = result//10
            return result
        else:
            print("How the hell should I get the input?")

    def solve_shortcut(self):
        """ 
            1. Let python do the thing
            2. Enjoy!
        """
        N = int(input().strip())
        return int(str(sum([int(input().strip()) for _ in range(N)]))[:10])


if __name__ == '__main__':
    brute_solver = BruteSolution()
    # brute_solver.solve_shortcut() #type in the inputs
    numbers = [
        37107287533902102798797998220837590246510135740250,
        46376937677490009712648124896970078050417018260538,
        74324986199524741059474233309513058123726617309629,
        91942213363574161572522430563301811072406154908250,
        23067588207539346171171980310421047513778063246676
    ]
    x = brute_solver.solve(is_io_input=False, numbers=numbers)
    print(x)