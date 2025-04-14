"""Test Module Models
=================

This module contains the test model that demonstrates Python 3.12 features.
"""

from odoo import fields, models


class TestModel(models.Model):
    """Test Model
    ==========

    This model demonstrates Python 3.12 features in Odoo.
    """

    _name = "test.model"

    name = fields.Char("Name")

    def test_method(self):
        """Test Method
        ==========

        This method demonstrates Python 3.12 pattern matching and type hints.
        """
        match = {
            "key": "value",
            "another": "data",
        }
        match match:
            case {"key": value}:
                print(f"Found key with value: {value}")  # noqa: T201
            case _:
                print("No match found")  # noqa: T201

    def another_method(self, param1: str, param2: int) -> bool:
        """Another Method
        ============

        This method demonstrates type hints and pattern matching.

        Args:
            param1: First parameter
            param2: Second parameter

        Returns:
            bool: Result of the operation

        """
        match (param1, param2):
            case ("test", 123):
                return True
            case _:
                return False
