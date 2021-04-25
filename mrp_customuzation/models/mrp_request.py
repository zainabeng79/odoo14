from odoo import models, fields, api

class MaintenanceReq(models.Model):
    _inherit = 'maintenance.request'
    requester_id = fields.Many2one('res.partner','created By')
    des_loc = fields.Many2one('res.partner','Destination Location')
    matrial_req_emp = fields.Many2one('res.partner','Matrial Requisition Employee')
    notebook_ids = fields.One2many('notebook.class', 'main_class_id', string="Notebook")
    sales_order_count = fields.Integer(compute='get_sales_order_count')
    state = fields.Selection([
        ('new_request', 'New Request'),
        ('first_approval', 'First Approval'),
        ('second_approval', 'Second Approval'),
        ('in_progress', 'In Progress'),
        ('repaired', 'Repaired'),
        ('scrap', 'Scrap'),
    ], default='new_request')

    # method for counting the number of orders
    # def get_sales_order_count(self):
    #     count = self.env['sale.order'].search_count([('partner_id','=',self.id)])
    #     self.sales_order_count=count

#     sales
    def create_so(self):
        print('aaqq')
        list = []
        for line in self.notebook_ids:
            list.append((0,0,{
                'name':line.name,
                'product_id': line.product_id.id,
                'product_uom_qty': line.product_uom_qty,
                'product_uom': line.product_uom.id,
                'price_unit': line.price_unit,
            }))
        sale_order = self.env['sale.order'].create({
            'partner_id': 1,
            'order_line': list,
        })
        line.quotation_created=True
        return {
            'type': 'ir.actions.act_window',
            'name': 'Selected Product',
            'view_mode': 'tree,form',
            'res_model': 'sale.order',
            'res_id': 'sale_order.id',
            'target': 'current',
        }
class NotebookClass(models.Model):
    _name = 'notebook.class'
    main_class_id = fields.Many2one('maintenance.request', string="Main Class")
    product_id = fields.Many2one('product.product', string='Product')
    name = fields.Text('Description')
    product_uom_qty = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure',)
    quotation_created = fields.Boolean(readonly=True)