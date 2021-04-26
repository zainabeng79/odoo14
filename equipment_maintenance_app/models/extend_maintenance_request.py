from odoo import models, fields


class MaintenanceChecklist(models.Model):
    _inherit = 'maintenance.request'
    company_id = fields.Many2one('res.company', string='Company')
    partner_id = fields.Many2one('res.partner', string='Customer')
    note = fields.Text()
    notebook_ids = fields.One2many('notebook.class', 'main_class_id', string="Notebook")

    # sales qutation
class NotebookClass(models.Model):
    _name = 'notebook.class'
    main_class_id = fields.Many2one('maintenance.request', string="Main Class")
    product_id = fields.Many2one('product.product', string='Product')
    description = fields.Text('Description')
    product_uom_qty = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Unit Price')

    # method for counting the number of orders
    # def get_sales_order_count(self):
    #     count = self.env['sale.order'].search_count([('partner_id', '=', self.id)])
    #     self.sales_order_count = count
