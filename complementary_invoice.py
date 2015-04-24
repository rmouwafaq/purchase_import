# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


string_tab = [('cout', "Cout"),('quantity', "Quantity"),]
class complementary_invoice(osv.osv):
    _name='complementary.invoice'
    
    _columns = { 
        'name'             : fields.char(string="Nom Facture", required=True),
        'supplier_invoice' : fields.many2one('account.invoice', string="Facture Origine"),
        'montant_id'       : fields.float(string="Montant"),
        'bursting_type'    : fields.selection(string_tab, string="Type Eclatement", default="cout"),
        'complementary_invoice_lines_ids' : fields.one2many('complementary.invoice.lines','complementary_invoice_id', string="Articles", required=True),
        'import_invoice_id': fields.many2one('import.invoice', string="Facture Import"),
                }
    
    def get_montant(self, cr, uid, ids, supplier_invoice, context = None): 
        values = {}
        inv = self.pool.get('account.invoice').browse(cr, uid, supplier_invoice)
        print inv
        mt = inv.amount_total
        values['montant_id'] = mt
        return {'value': values}
    
   
  