# # my_module_2/models/account.py
from odoo import models, fields

class AccountTransaction(models.Model):
    _name = 'account.transaction'
    _description = 'Accounting Transaction'

    name = fields.Char(string='Transaction Name')
    amount = fields.Float(string='Amount')
    date = fields.Date(string='Transaction Date')
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled')
    ], default='draft')
    account_id = fields.Many2one('account.account', string='Account')

    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'

    def action_cancel(self):
        for record in self:
            record.state = 'canceled'

# from odoo import models, fields

# class AccountTransaction(models.Model):
#     _name = 'account.transaction'
#     _description = 'Accounting Transaction'

#     name = fields.Char(string='Transaction Name')
#     amount = fields.Float(string='Amount')
#     date = fields.Date(string='Date')
#     description = fields.Text(string='Description')
#     state = fields.Selection([
#         ('draft', 'Draft'),
#         ('confirmed', 'Confirmed'),
#     ], default='draft', string='State')
#     account_id = fields.Many2one('account.account', string='Account')

#     def action_confirm(self):
#         for record in self:
#             record.state = 'confirmed'

#     def action_cancel(self):
#         for record in self:
#             record.state = 'canceled'