import string
import random

from odoo import api,fields,models
from datetime import datetime, date, timedelta

class ClientSubscription(models.Model):
    _name = 'client.subscription'
    _description = 'Client Subscription'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # fields declaration
    name = fields.Char(string='Name')
    subscription_code = fields.Char(
        string='UUID',
        size=10,
        unique=True,
        default=lambda self: self._generate_sucscription_code()
    )
    subscription_start_date = fields.Date(string='Subscription Date')
    subscription_end_date = fields.Date(string='Subscription End Date')
    active = fields.Boolean(string='Active', default=True, readonly=True)

    @api.model
    # random generate uuid
    def _generate_sucscription_code(self):
        """Generate a random string of size 10."""
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
