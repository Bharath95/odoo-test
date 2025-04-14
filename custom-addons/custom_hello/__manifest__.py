"""
Custom Hello Module Manifest
==========================

This manifest file defines the basic information about the custom hello module.
"""

{
    'name': 'Custom Hello',
    'version': '18.0.1.0.0',
    'category': 'Uncategorized',
    'summary': (
        'Custom Hello World Module that demonstrates basic Odoo module '
        'structure and functionality'
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
