# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class import_invoice(osv.osv):
    _name = 'import.invoice' 
    
    _columns = {  
        'name' : fields.char(string="Nom Facture", required=True),           
        'account_id' : fields.many2one('account.invoice', string="Facture Achat"),
        'dossier_import_id' : fields.many2one("dossier.import", string="Dossier Import"),
        'complementary_invoice_ids' : fields.one2many('complementary.invoice','import_invoice_id', string="Facture Complementaire"),
        'import_invoice_lines_ids' : fields.one2many('import.invoice.lines','import_invoice_id', string="Articles"),   
            }
    
    def state_id_change(self, cr, uid, ids, account_id, context = None): 
        values = {}
        fact_imp_line_obj= self.pool.get('import.invoice.lines')
        print fact_imp_line_obj
        inv = self.pool.get('account.invoice').browse(cr, uid, account_id)
        print inv
        factre_improt_line_ids=[]
        for line in inv.invoice_line:
            vals={}
            print 'product id :',line.product_id.id
            print 'product price :',line.product_id.product_tmpl_id.list_price
            vals['itms_id']=line.product_id.id
            print "vals['itms_id']==",vals['itms_id']
            vals['montant_achat']= line.price_subtotal
            print "vals['montant_achat']==",vals['montant_achat']
            id=fact_imp_line_obj.create(cr, uid,vals)
            print "ID==",id
            factre_improt_line_ids.append(id)
        values['import_invoice_lines_ids']=factre_improt_line_ids
        return {'value': values}
    
    
    
        