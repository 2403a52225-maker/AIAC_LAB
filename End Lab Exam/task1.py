"""
question1_clean_email_unittest.py

Contains:
- clean_email_data: cleans a list of email addresses (lowercase, trim, dedupe, preserve order)
- Unittest test cases for clean_email_data

Run:
    python question1_clean_email_unittest.py
"""

from typing import List
import unittest


def clean_email_data(emails: List[str]) -> List[str]:
    """
    Clean a list of email addresses.

    Steps:
      - Ignore None values
      - Strip leading/trailing whitespace
      - Convert to lowercase
      - Remove duplicates while preserving the order of first appearance
      - Skip empty strings after trimming

    Args:
        emails: List[str] - raw email strings

    Returns:
        List[str]: cleaned, unique emails in original order
    """
    cleaned: List[str] = []
    seen = set()

    for raw in emails:
        # Defensive: skip None
        if raw is None:
            continue

        # Trim whitespace and convert to lowercase
        email = raw.strip().lower()

        # Skip empty strings
        if not email:
            continue

        # Add if not seen already (preserve first occurrence)
        if email not in seen:
            seen.add(email)
            cleaned.append(email)

    return cleaned


class TestCleanEmailData(unittest.TestCase):
    def test_basic_cleanup_and_dedup(self):
        inp = [
            " Alice@Example.com ",
            "BOB@example.COM",
            "alice@example.com",     # duplicate of first when cleaned
            "   ",                   # blank (should be ignored)
            None,                    # should be ignored
            "charlie@EXAMPLE.com"
        ]
        expected = ["alice@example.com", "bob@example.com", "charlie@example.com"]
        self.assertEqual(clean_email_data(inp), expected)

    def test_preserve_order(self):
        inp = ["b@e.com", "A@E.com", "a@e.com", "c@e.com", "B@E.com"]
        # first unique occurrences of cleaned emails: b@e.com, a@e.com, c@e.com
        expected = ["b@e.com", "a@e.com", "c@e.com"]
        self.assertEqual(clean_email_data(inp), expected)

    def test_all_empty_or_none(self):
        self.assertEqual(clean_email_data([" ", "", "   ", None]), [])

    def test_mixed_types_strict(self):
        # ensure function is robust for typical misuse (non-str types raise AttributeError)
        with self.assertRaises(AttributeError):
            clean_email_data([123, "a@b.com"])  # ints don't have strip() -> raises


if __name__ == "__main__":
    unittest.main(verbosity=2)
