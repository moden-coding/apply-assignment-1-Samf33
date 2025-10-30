import unittest
import pandas as pd
import numpy as np
import apply_assign

# --- Re-create the dataset ---
df_base = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David", "Ella", "Frank"],
    "Exam_Score": [85, 72, 90, 64, 78, 95],
    "Study_Hours": [6, 3, 8, 2, 4, 10],
    "Attendance": [0.95, 0.80, 0.90, 0.70, 0.75, 0.98]
})


# --- UNIT TESTS ---
class TestApplyMethods(unittest.TestCase):

    def setUp(self):
        """Fresh copy of data for each test"""
        self.df = df_base.copy()

    def test_assign_letter_grades(self):
        result = apply_assign.assign_letter_grades(self.df)
        expected = ["B", "C", "A", "D", "C", "A"]
        self.assertListEqual(list(result["Grade"]), expected)

    def test_calculate_adjusted_score(self):
        result = apply_assign.calculate_adjusted_score(self.df)
        expected = [
            85 + (6 * 1.5) + (0.95 * 10),   # Alice
            72 + (3 * 1.5) + (0.80 * 10),   # Bob
            90 + (8 * 1.5) + (0.90 * 10),   # Charlie
            64 + (2 * 1.5) + (0.70 * 10),   # David
            78 + (4 * 1.5) + (0.75 * 10),   # Ella
            95 + (10 * 1.5) + (0.98 * 10)   # Frank
        ]
        np.testing.assert_almost_equal(result["Adjusted_Score"], expected, decimal=1)

    def test_categorize_performance(self):
        graded = apply_assign.assign_letter_grades(self.df.copy())
        adjusted = apply_assign.calculate_adjusted_score(graded)
        result = apply_assign.categorize_performance(adjusted)
        expected = ["Strong", "Needs Improvement", "Outstanding", "Needs Improvement", "Needs Improvement", "Outstanding"]
        self.assertListEqual(list(result["Performance"]), expected)


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
