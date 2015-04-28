# -*- coding: utf-8 -*-
{
    "name": "Gestion Multi-Magasins",
    "version": "1.0",
    "category": "Test",
    'sequence': 1,
    'summary': """Calcul Cout d'Achat des Articles""",
    "depends": ["base","purchase","product"],
    'description': """
        L'importation
    """,
    'author': "Abdelaziz",
    'website': "http://www.agilorg.com",
    "data": [
        "view/menu.xml",     
        "view/complementary_invoice.xml",
        "view/complementary_invoice_lines.xml",
        "view/import_invoice.xml",
        "view/import_invoice_lines.xml",
        "view/dossier_import.xml",
        "wizard/create_facture_view.xml",
    ],
    "css":['static/src/css/allign.css'],
    "demo": [],
    "test": [],
    "installable": True,
    "auto_install": False,
}