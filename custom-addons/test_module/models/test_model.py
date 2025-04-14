from odoo import models, fields

class TestModel(models.Model):
    _name = 'test.model'
    
    name = fields.Char('Name')
    
    def test_method(self):
        # Missing docstring
        return True
    
    def another_method(self, param1, param2, param3, param4, param5):
        # Too many arguments
        return True
    
    def yet_another_method(self):
        # Long line
        this_is_a_very_long_variable_name = "This is a very long string that will definitely exceed the 120 character limit and trigger a linting error"
        return True
