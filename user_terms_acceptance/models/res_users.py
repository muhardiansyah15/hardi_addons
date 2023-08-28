# Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
# Copyright (C) Thinkopen Solutions <http://www.tkobr.com>.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api
from odoo.addons.base.models.ir_cron import _intervalTypes
from odoo.http import request
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class ResUsers(models.Model):
    _inherit = 'res.users'
    
    tnc_acceptance = fields.Boolean('User Terms Acceptance')