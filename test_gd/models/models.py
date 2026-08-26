from odoo import api, fields, models, _


class Column(models.Model):
    _name = 'test_gd.column'
    _description = 'Columns'

    name = fields.Char('Name')
    column_type = fields.Char('Column Type')


class Data(models.Model):
    _name = 'test_gd.data'
    _description = 'General Data'

    name = fields.Char('Name', help='Data Name')
    source_application = fields.Char('Source')
    api_url = fields.Char('API')
    column_ids = fields.Many2many('test_gd.column', 'Columns')
