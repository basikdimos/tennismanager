# -*- coding: utf-8 -*-

# 1 : imports of python lib
import logging, datetime

# 2 :  imports of odoo
from odoo import api, fields, models

# 3 :  imports of odoo modules

# 4 :  imports from custom modules

_logger = logging.getLogger(__name__)

class AbonimentModel(models.Model):
    """ 
    Модель Абонимент
    """ 

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'golden_ball.aboniment_model'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------
    name = fields.Many2one(
        'golden_ball.aboniment_type_model',
        string = "Тип абонимента",
    )

    aboniment_id = fields.Many2one(
        'golden_ball.client_model',
        string="Parent client"
    )

    date_begin = fields.Date(
        string = "Дата начала",
        #default = lambda self: datetime.date.today()
    )

    date_end = fields.Date(
        string = "Дата окончания",
        default = lambda self : datetime.date.today()  + datetime.timedelta(days=31)
    )

    number_visits = fields.Integer(
        string = 'Количество посещений',
        default = 1
    )

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------

    # Action methods
    # ------------------------------------------------------------------------------------------------------------------

    # Business methods
    # ------------------------------------------------------------------------------------------------------------------

    # CRUD methods
    # ------------------------------------------------------------------------------------------------------------------