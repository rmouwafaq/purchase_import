# -*- coding: utf-8 -*-
from openerp.osv import fields, osv



class complementary_invoice_lines(osv.osv):
    _name='complementary.invoice.lines'
    _columns = {        
        'itms_id' : fields.many2one('product.product', string="Articles", readonly=True),
        'montant_id' : fields.float(string="Montant", readonly=True), 
        'complementary_invoice_id' : fields.many2one("complementary.invoice", string="Facture complémentaire", readonly=True)      
                }