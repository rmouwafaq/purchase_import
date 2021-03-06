# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class import_invoice(osv.osv):
    _name = 'import.invoice' 
    
    _columns = {  
                
        'name' : fields.char(string="Nom Facture", required=True),           
        'account_id' : fields.many2one('account.invoice', string="Facture Achat", required=True),
        'dossier_import_id' : fields.many2one("dossier.import", string="Dossier Import"),
        'complementary_invoice_ids' : fields.one2many('complementary.invoice','import_invoice_id', string="Facture Complementaire"),
        'import_invoice_lines_ids' : fields.one2many('import.invoice.lines','import_invoice_id', string="Articles"),   
            
            }
    
    
    def calcul_prix_vente(self, cr, uid, account_id, vals, context = None):
        inv = self.pool.get('import.invoice').browse(cr, uid, account_id)['import_invoice_lines_ids']
        prds = self.pool.get('product.product')
        for line in inv:
            line.itms_id.margin = line.margin
            line.itms_id.lst_price = line.sale_price
        return True
    
    def create(self, cr, uid, vals, context = None): 
        v=vals['account_id']
        complementary_invoice_ids=vals['complementary_invoice_ids'][0][2]
        print complementary_invoice_ids
        brws=self.pool.get('complementary.invoice').browse(cr, uid, complementary_invoice_ids)
        fact_imp_line_obj= self.pool.get('import.invoice.lines')
        inv = self.pool.get('account.invoice').browse(cr, uid, v)
        prds = self.pool.get('product.product')
        factre_improt_line_ids=[]
        val={}
        mt_hors_tax = inv.amount_untaxed
        qty = 0
        for qt in inv.invoice_line:
            qty += qt.quantity
        for line in inv.invoice_line:
                mt_frais =0
                for rec in brws:
                    ecl = rec.bursting_type
                    if ecl == "cout":
                        mt_frais += ((rec.montant_id * line.price_subtotal) / mt_hors_tax)
                    else:
                        mt_frais += ((rec.montant_id * line.quantity) / qty) 
                pr = prds.browse(cr, uid,line.product_id.id)
                print 'margin',pr.margin            
                val['itms_id']=line.product_id.id
                val['quantity']= line.quantity
                val['montant_achat']= line.price_subtotal
                val['montant_frais']= mt_frais
                val['montant_global']= (val['montant_achat'] + val['montant_frais'])
                val['prix_article']=(val['montant_global'] / line.quantity)
                val['margin'] = pr.margin
                val['sale_price'] = ((val['prix_article']+(val['prix_article'] * val['margin'])/100))
                print "val article:",val['prix_article']
                id=fact_imp_line_obj.create(cr, uid,val)
                factre_improt_line_ids.append(id)   
                vals['import_invoice_lines_ids']=[[6, False, factre_improt_line_ids]]
        return super(import_invoice, self).create(cr, uid, vals, context)
    
    
    
    
    def write(self, cr, uid, ids, vals, context = None):
        print vals
        print ids
        complementary_invoice_ids=vals['complementary_invoice_ids'][0][2]
        brws=self.pool.get('complementary.invoice').browse(cr, uid, complementary_invoice_ids)
        fact_imp_line_obj= self.pool.get('import.invoice.lines')
        inv = self.pool.get('import.invoice').browse(cr, uid, ids)['account_id']
        prds = self.pool.get('product.product')
        factre_improt_line_ids=[]
        val={}
        mt_hors_tax = inv.amount_untaxed
        print mt_hors_tax
        qty =0
        for qt in inv.invoice_line:
            qty += qt.quantity
        print qty   
        for line in inv.invoice_line:  
            mt_frais =0
            for rec in brws:
                ecl = rec.bursting_type
                if ecl == "cout":
                        mt_frais += ((rec.montant_id * line.price_subtotal) / mt_hors_tax)
                    
                else:
                        mt_frais += ((rec.montant_id * line.quantity) / qty) 
            pr = prds.browse(cr, uid,line.product_id.id)
            print 'margin',pr.margin                         
            val['itms_id']=line.product_id.id
            val['quantity']= line.quantity
            val['montant_achat']= line.price_subtotal
            val['montant_frais']= mt_frais
            val['montant_global']= (val['montant_achat'] + val['montant_frais'])
            val['prix_article']=(val['montant_global'] / line.quantity)
            val['margin'] = pr.margin
            val['sale_price'] = ((val['prix_article'] * val['margin'])/100)
            id=fact_imp_line_obj.create(cr, uid,val)
            factre_improt_line_ids.append(id)    
            vals['import_invoice_lines_ids']=[[6, False, factre_improt_line_ids]] 
        return super(import_invoice, self).write(cr, uid, ids, vals, context)
        