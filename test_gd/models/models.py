from odoo import api, fields, models, _


class Columns(models.Model):
    _name = 'test_gd.columns'
    _description = 'Columns'

    name = fields.Char('Name')
    column_type = fields.Char('Column Type')


class Data(models.Model):
    _name = 'test_gd.data'
    _description = 'General Data'

    name = fields.Char('Name', help='Data Name')
    source_application = fields.Char('Source')
    api_url = fields.Char('API')
    columns = fields.One2many('test_gd.columns', 'Columns')
