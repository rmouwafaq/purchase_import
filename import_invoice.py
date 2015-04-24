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
        v=vals['account_id']
        complementary_invoice_ids=vals['complementary_invoice_ids'][0][2]
        brws=self.pool.get('complementary.invoice').browse(cr, uid, complementary_invoice_ids)
        fact_imp_line_obj= self.pool.get('import.invoice.lines')
        inv = self.pool.get('account.invoice').browse(cr, uid, v)
        factre_improt_line_ids=[]
        val={}
        mt_frais =0
        for line in inv.invoice_line:
                for rec in brws:
                    print rec
                    ecl = rec.bursting_type
                    if ecl == "cout":
                        mt_frais += rec.montant_id / line.price_subtotal
                    else :
                        mt_frais += rec.montant_id / line.quantity
                val['itms_id']=line.product_id.id
                print val['itms_id']
                val['montant_achat']= line.price_subtotal
                print val['montant_achat']
                val['montant_frais']= val['montant_achat']+mt_frais
                print val['montant_frais']
                id=fact_imp_line_obj.create(cr, uid,val)
                print "ID==",id
                factre_improt_line_ids.append(id)    
        vals['import_invoice_lines_ids']=[[6, False, factre_improt_line_ids]]
        print "sortie ",vals
        #print vals['import_invoice_lines_ids']
        #print factre_improt_line_ids
        return super(import_invoice, self).create(cr, uid, vals, context)
    
    
    
        