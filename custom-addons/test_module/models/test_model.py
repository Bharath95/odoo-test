from odoo import models, fields

class TestModel(models.Model):
    _name = 'test.model'
    
    name = fields.Char('Name')
    
    def test_method(self):
        """Test method with Python 3.12 features."""
        match = {
            'key': 'value',
            'another': 'data'
        }
        match match:
            case {'key': value}:
                print(f"Found key with value: {value}")
            case _:
                print("No match found")
    
    def another_method(self, param1: str, param2: int) -> bool:
        """Method with type hints and pattern matching."""
        match (param1, param2):
            case ('test', 123):
                return True
            case _:
                return False
