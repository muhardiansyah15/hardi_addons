# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from datetime import datetime
import odoo
import pytz
from dateutil.relativedelta import relativedelta
from odoo import http, fields, SUPERUSER_ID, _
from odoo.http import request, route
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.addons.web.controllers.home import Home
from odoo.addons.web.controllers.session import Session
from odoo.addons.web.controllers.action import Action
from odoo.addons.web.controllers.utils import clean_action


_logger = logging.getLogger(__name__)


class HomeTnc(Home):

    @http.route()
    def web_login(self, *args, **kw):
        print("WKWKWKWWKHAHAHAAHAHAHAHA = = \n\n\n\n")
        return super().web_login(*args, **kw)