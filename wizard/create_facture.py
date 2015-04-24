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
        fact_comp_line_obj= self.pool.get('complementary.invoice')
        print fact_comp_line_obj
        brws_list=fact_comp_line_obj.browse(cr, uid, ids)
        print brws_list
        print brws_list.id
        for brws in brws_list:
            print brws.name
            
                                           
                                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """def action_add_factures(self, cr, uid, ids,vals, context = None):
        print "context==",context
        print vals
        brws_list= self.browse(cr, uid, ids)
        print "ids",ids
        print brws_list
        list_ids=[]
        for brws in brws_list:
            print brws.name
            print brws.account_id
            print brws.complementary_invoice_ids
            for complementary_invoice_id in brws.complementary_invoice_ids:
                list_ids.append(complementary_invoice_id.id)
            print list_ids
        invs = self.pool.get('complementary.invoice').browse(cr, uid, complementary_invoice_ids)
        for line in invs :
            print line.name
        return True"""
        