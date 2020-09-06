# -*- coding: utf-8 -*-
{
    "name": """Gantt Native view for Projects EE""",
    "summary": """Tehnical Module for EE version for Same view Standart Gantt and Gantt Native""",
    "category": "Project",
    "images": ['static/description/banner.gif'],
    "version": "13.20.05.11.0",
    "description": """

    """,
    "author": "Viktor Vorobjov",
    "license": "OPL-1",
    "website": "https://straga.github.io",
    "support": "vostraga@gmail.com",
    "live_test_url": "https://demo13.garage12.eu",

    "depends": [
        "project_native",
        "project_enterprise",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'views/project_ee_view.xml',
    ],
    "qweb": [],
    "demo": [],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
    "application": False,
}
