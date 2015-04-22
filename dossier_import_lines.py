# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class dossier_import_lines(osv.osv):
    _name = 'dossier.import.lines' 
    
    _columns = {                  
        'itms_id' : fields.many2one('product.product', string="Articles"),
        'montant_id' : fields.float(string="Montant"),
               }