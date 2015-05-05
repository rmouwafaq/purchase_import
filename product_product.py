# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class product_product(osv.osv):
    _inherit = 'product.product'
    
    _columns = {
                
    'margin': fields.float(string="Marge"),
    'public_price': fields.float(string='Prix public', readonly=True),
    'basic_price': fields.float(string='Prix Base')
    
                }
    
    
    
    def write(self, cr, uid, ids, vals, context = None):
        print vals
        prds = self.pool.get('product.product').browse(cr, uid, ids)
        vals['public_price'] = prds.basic_price + vals['margin']
        return super(product_product, self).write(cr, uid, ids, vals, context)