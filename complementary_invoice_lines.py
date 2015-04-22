# -*- coding: utf-8 -*-
from openerp.osv import fields, osv



class complementary_invoice_lines(osv.osv):
    _name='complementary.invoice.lines'
    _columns = {        
        'itms_id' : fields.many2one('product.product', string="Articles"),
        'montant_id' : fields.float(string="Montant"), 
        'complementary_invoice_id' : fields.many2one("complementary.invoice", string="Facture complémentaire")      
                }