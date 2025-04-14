"""
Test Module Manifest
===================

This manifest file defines the basic information about the test module.
"""

{
    'name': 'Test Module',
    'version': '18.0.1.0.0',
    'category': 'Uncategorized',
    'summary': (
        'Test module for Python 3.12 features that demonstrates modern Python '
        'features and Odoo integration'
    ),
    'author': 'Odoo Community Association (OCA)',
    'maintainer': 'Odoo Community Association (OCA)',
    'website': 'https://odoo-community.org/',
    'depends': ['base'],
    'data': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'post_init_hook': 'post_init',
}
