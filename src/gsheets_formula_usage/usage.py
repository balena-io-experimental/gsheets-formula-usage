"""Utilities to parse the usage-related information."""
import string


class Index:
    """Class to manage the indexing of values within spreadsheets."""

    alphabet = string.ascii_uppercase

    @staticmethod
    def to_number(value: int) -> int:
        """Convert value to its 1-based index."""
        return value + 1

    @staticmethod
    def to_letter(value: int) -> str:
        """Convert value to its alphabetical index."""
        divisor, remainder = divmod(value, len(Index.alphabet))
        return Index.to_letter(divisor - 1) + Index.alphabet[remainder] if divisor else Index.alphabet[remainder]
