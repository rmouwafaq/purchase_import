# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class import_invoice_lines(osv.osv):
    _name = 'import.invoice.lines' 
    
    _columns = {            
        'itms_id' : fields.many2one('product.product', string="Articles",ondelete='cascade', index=True, readonly=True),
        'quantity': fields.float(string="Quantité", readonly=True),
        'montant_achat' : fields.float(string="Montant Achat", readonly=True),
        'montant_frais' : fields.float(string="Montant Frais", readonly=True),
        'montant_global': fields.float(string="Cout Achat Global", readonly=True),
        'prix_article'  : fields.float(string="Cout Achat Unitaire", readonly=True),
        'margin'        : fields.float(string="Marge", readonly=True),
        'sale_price'    : fields.float(string="Prix Vente", readonly=True),
        'import_invoice_id' : fields.many2one("import.invoice", string="Facture Import", readonly=True)
            }
    
    
