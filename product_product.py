# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class product_product(osv.osv):
    _inherit = 'product.product'
    
    _columns = {
                
    'margin': fields.float(string="Marge"),
    'public_price': fields.float(string='Prix public', readonly=True),
    'basic_price': fields.float(string='Prix Base')
    
                }
    
    
    
    