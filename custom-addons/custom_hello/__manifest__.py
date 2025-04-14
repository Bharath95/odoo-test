{
    'name': 'Custom Hello',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'A simple Hello World module',
    'description': """
        This is a simple module that demonstrates the basic structure of an Odoo module.
        It creates a simple model and a view to display a message.
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'views/hello_view.xml',
    ],
    'installable': True,
    'application': False,
}
