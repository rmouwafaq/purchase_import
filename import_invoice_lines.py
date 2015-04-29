# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class import_invoice_lines(osv.osv):
    _name = 'import.invoice.lines' 
    
    _columns = {            
        'itms_id' : fields.many2one('product.product', string="Articles",ondelete='cascade', index=True),
        'quantity': fields.float(string="Quantité"),
        'montant_achat' : fields.float(string="Montant Achat"),
        'montant_frais' : fields.float(string="Montant Frais"),
        'montant_global': fields.float(string="Cout Achat Global"),
        'prix_article'  : fields.float(string="Cout Achat Unitaire"),
        'import_invoice_id' : fields.many2one("import.invoice", string="Facture Import")
            }