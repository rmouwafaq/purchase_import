# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class CreateFactureWizard(osv.TransientModel):
    _name ='gestion_multi_magasins.create_facture_wizard' 
    _columns = {  
        'name' : fields.char(string="Nom Facture", required=True),           
        'account_id' : fields.many2one('account.invoice', string="Facture Achat"), 
        'complementary_invoice_ids' : fields.one2many('complementary.invoice','id', string="Facture Complementaire"),
            }
    
    
    def action_add_factures(self, cr, uid, ids, context = None): 
        inv = self.pool.get('account.invoice').browse(cr, uid,ids)
        for line in inv :
            print line
        return True
        