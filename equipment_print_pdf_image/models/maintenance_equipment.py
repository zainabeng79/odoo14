# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MaintenanceEquipmentInherit(models.Model):
    _inherit = 'maintenance.equipment'

    image1 = fields.Binary('Image1')
    image2 = fields.Binary('Image2')
    image3 = fields.Binary('Image3')
    image4 = fields.Binary('Image4')
    image5 = fields.Binary('Image5')
    image6 = fields.Binary('Image6')

