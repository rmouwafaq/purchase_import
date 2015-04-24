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
    
    def create(self, cr, uid, vals, context = None): 
        print "entree :",vals
        v=vals['account_id']
        fact_imp_line_obj= self.pool.get('import.invoice.lines')
        print fact_imp_line_obj
        inv = self.pool.get('account.invoice').browse(cr, uid, v)
        print inv
        factre_improt_line_ids=[]
        for line in inv.invoice_line:
            val={}
            print 'product id :',line.product_id.id
            print 'quantity of product : ',line.quantity
            print 'product price :',line.product_id.product_tmpl_id.list_price
            val['itms_id']=line.product_id.id
            print "vals['itms_id']==",val['itms_id']
            val['montant_achat']= line.price_subtotal
            print "vals['montant_achat']==",val['montant_achat']
            id=fact_imp_line_obj.create(cr, uid,val)
            print "ID==",id
            factre_improt_line_ids.append(id)
        vals['import_invoice_lines_ids']=[[6, False, factre_improt_line_ids]]
        #print vals['import_invoice_lines_ids']
        #print factre_improt_line_ids
        print "sortie :",vals
        return super(import_invoice, self).create(cr, uid, vals, context)
    
    
    
        