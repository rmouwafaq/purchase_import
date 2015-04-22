# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class dossier_import(osv.osv):
    _name = 'dossier.import' 
    
    _columns = { 
        'name' : fields.char(string="Nom Dossier"), 
        'active' : fields.boolean(string="Active"), 
        'import_invoice_lines_ids' : fields.one2many('import.invoice','dossier_import_id', string="Facture Import"),       
                }