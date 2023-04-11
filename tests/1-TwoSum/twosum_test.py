import unittest
from python.src import twosum_2

class Test_TwoSum(unittest.TestCase):
    def setUp(self):
        self.s = twosum_2.Solution()
        self.numbers = [[2,7,11,15], [3, 2, 4], [3, 3]]
        self.targets = [9, 6, 6]
        self.solutions = [[[0,1], [1,0]], [[1, 2], [2, 1]], [[0, 1], [1, 0]]]
             
    def testCorrectness(self):
        for i in range(len(self.numbers)):
            solutions = self.solutions[i]
            answer = self.s.twoSum(self.numbers[i], self.targets[i])
            self.assertIn(answer, solutions)
    
if __name__ == '__main__':
    unittest.main()