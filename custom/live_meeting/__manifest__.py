# -*- coding: utf-8 -*-
{
    'name': 'Live Meeting',
    'version': '1.0',
    'category': 'Productivity/Discuss',
    'sequence': 10,
    'summary': 'Live Meeting, chat, mail gateway and private channels',
    'description': "",
    'website': 'https://www.odoo.com/app/discuss',
    'depends': ['base', 'base_setup', 'bus', 'web_tour', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/schedule.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'demo': [],

    'assets': {
       'web.assets_backend': [
            '/live_meeting/static/src/js/meeting.js',
        ],

        'web.assets_common': [

        ],
    },
}
