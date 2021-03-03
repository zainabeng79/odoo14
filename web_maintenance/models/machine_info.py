# -*- coding: utf-8 -*-
from odoo import api, fields, models


class MachineInfo(models.Model):
    _name = 'machine.info'
    _rec_name = 'Machine_Name'
    _description = 'Machine Info'

    Machine_Name = fields.Char(string="Machine Name", required=False)
    Machine_ShortName = fields.Char(string="Machine ShortName", required=False)
    Machine_Code = fields.Char(string="Machine Code", required=False)
    BAMS_Mac_Code = fields.Char(string="BAMS Mac Code", required=False)
    BAMS_Mac_Desc = fields.Char(string="BAMS Mac Desc", required=False)
