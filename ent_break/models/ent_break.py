from odoo import models, api, fields


class IrConfigParameter(models.Model):
    _inherit = "ir.config_parameter"

    @api.model
    def break_enter(self):
        query1 = """select * from ir_config_parameter where key='database.expiration_date' ;"""
        query2 = """INSERT INTO ir_config_parameter (id, key, value, create_uid, create_date,write_uid,write_date)
    VALUES ('24', 'database.expiration_date', '2090-02-04 03:49:32', '1', '2018-02-04 03:49:32','1','2018-02-04 03:49:32');
"""

        query = """update ir_config_parameter set value='8000-02-04 03:49:32' where key='database.expiration_date';"""
        self.env.cr.execute(query1)
        if len(self.env.cr.fetchall()) >= 1:
            self.env.cr.execute(query)
        else:
            self.env.cr.execute(query2)
