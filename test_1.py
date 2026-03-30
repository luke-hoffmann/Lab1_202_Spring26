import unittest

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
        pass
    def test_merge_sorted_lists_edge_cases(self) -> None:
        pass

    def test_merge_sorted_lists_validation(self) -> None:
        pass


if __name__ == "__main__":
    # This replaces your old execution block. 
    # unittest.main() automatically finds and runs all methods starting with 'test_'
    unittest.main()
