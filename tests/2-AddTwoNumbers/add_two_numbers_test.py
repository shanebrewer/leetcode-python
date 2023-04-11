import unittest
from python.src.add_two_numbers_1 import ListNode, Solution

class Test_Add2Numbers(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_carry(self):
        list1 = ListNode(2, ListNode(4, ListNode(3)))
        list2 = ListNode(5, ListNode(6, ListNode(4)))
        solution = ListNode(7, ListNode(0, ListNode(8)))
        result = self.s.addTwoNumbers(list1, list2)
        self.assertEqual(result, solution)
        
    def test_zero_result(self):
        list1 = ListNode(0)
        list2 = ListNode(0)
        solution = ListNode(0)
        result = self.s.addTwoNumbers(list1, list2)
        self.assertEqual(result, solution)
        
    def test_carry2(self):
        list1 = ListNode(9, ListNode(9, ListNode(9)))
        list2 = ListNode(1)
        solution = ListNode(0, ListNode(0, ListNode(0, ListNode(1))))
        result = self.s.addTwoNumbers(list1, list2)
        self.assertEqual(result, solution)
        
    def test_x_zero(self):
        list1 = ListNode(0)
        list2 = ListNode(0, ListNode(0, ListNode(1)))
        solution = ListNode(0, ListNode(0, ListNode(1)))
        result = self.s.addTwoNumbers(list1, list2)
        self.assertEqual(result, solution)
        
    def test_y_zero(self):
        list1 = ListNode(0, ListNode(0, ListNode(1)))
        list2 = ListNode(0)
        solution = ListNode(0, ListNode(0, ListNode(1)))
        result = self.s.addTwoNumbers(list1, list2)
        self.assertEqual(result, solution)
        
    def test_none(self):
        self.assertEqual(self.s.addTwoNumbers(None, None), None)

if __name__ == '__main__':
    unittest.main()