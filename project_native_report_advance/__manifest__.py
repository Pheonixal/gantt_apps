# -*- coding: utf-8 -*-
{
    "name": """Gantt Native PDF Advance""",
    "summary": """Added support Gantt""",
    "category": "Project",
    "images": ['static/description/banner.gif'],
    "version": "13.20.06.16.0",
    "description": """
        PDF report use pycairo for draw/
        
    """,
    "author": "Viktor Vorobjov",
    "license": "OPL-1",
    "website": "https://www.youtube.com/watch?v=xbAoC_s5Et0&list=PLmxcMU6Ko0NkqpGLcC44_GXo3_41pyLNx",
    "live_test_url": "https://demo13.garage12.eu",
    "support": "vostraga@gmail.com",

    "depends": [
        "project",
        "project_native",
        "web_gantt_native",
    ],
    "external_dependencies": {"python": ["cairo"], "bin": []},
    "data": [

        'wizard/project_native_pdf_view.xml',
        'security/ir.model.access.csv',

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
