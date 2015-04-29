# -*- coding: utf-8 -*-
from openerp.osv import osv, fields



class product_product(osv.osv):
    _inherit = 'product.product'
    
    _columns = {
                
    'margin': fields.float(string="Marge"),
    
                }
    
    
    
    def create(self, cr, uid, vals, context = None):
        print self.margin
        return super(product_product, self).create(cr, uid, vals, context)