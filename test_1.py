import unittest
from lab1 import linear_search, Student, merge_sorted_lists
class TestLab1(unittest.TestCase):
    
    # --- Tests for Task 2: Linear Search ---
    
    def test_linear_search_typical(self) -> None:
        self.assertEqual(linear_search([10, 20, 30, 40, 50], 30), 2)
        self.assertEqual(linear_search([10, 20, 30, 40, 50], 10), 0)
        self.assertEqual(linear_search([10, 20, 30, 40, 50], 50), 4)

    def test_linear_search_edge_cases(self) -> None:
        self.assertEqual(linear_search([10, 20, 30], 99), -1) # Not in list
        self.assertEqual(linear_search([], 5), -1)            # Empty list
        self.assertEqual(linear_search([7, 8, 7, 9], 7), 0)   # Multiple occurrences


    # --- Tests for Task 3: Dataclass ---

    def test_student_dataclass(self) -> None:
        s1 = Student("Alice", 12345, 3.8)
        self.assertEqual(s1.name, "Alice")
        self.assertEqual(s1.id_number, 12345)
        self.assertEqual(s1.gpa, 3.8)

        s2 = Student("Alice", 12345, 3.8)
        s3 = Student("Bob", 67890, 3.2)
        
        # Dataclasses automatically implement __eq__ for comparing fields
        self.assertEqual(s1, s2)
        self.assertNotEqual(s1, s3)

    # --- Tests for Task 4: Merge Sorted Lists ---

    def test_merge_sorted_lists_typical(self) -> None:
        self.assertEqual(merge_sorted_lists([1],[5]),[1,5])
        self.assertEqual(merge_sorted_lists([1,2],[3,5]),[1,2,3,5])
        self.assertEqual(merge_sorted_lists([1,5,7,8],[2,5,6,7]),[1,2,5,5,6,7,7,8])
        self.assertEqual(merge_sorted_lists([10,20,50],[5,15,100]),[5,10,15,20,50,100])
    def test_merge_sorted_lists_edge_cases(self) -> None:
        self.assertEqual(merge_sorted_lists([],[]),[])
        self.assertEqual(merge_sorted_lists([1,2,3],[5]),[1,2,3,5])
        self.assertEqual(merge_sorted_lists([1],[4,5,5]),[1,4,5,5])
        self.assertEqual(merge_sorted_lists([9,10],[5]),[5,9,10])
        

    def test_merge_sorted_lists_validation(self) -> None:
        self.assertRaises(TypeError,merge_sorted_lists,"string",1234)
        self.assertRaises(TypeError,merge_sorted_lists,1,"string")
        self.assertRaises(TypeError,merge_sorted_lists,"string","abc123")

if __name__ == "__main__":
    # This replaces your old execution block. 
    # unittest.main() automatically finds and runs all methods starting with 'test_'
    unittest.main()
    
    


