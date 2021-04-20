# -*- coding: utf-8 -*-

# 1 : imports of python lib
import logging

# 2 :  imports of odoo
from odoo import api, fields, models

# 3 :  imports of odoo modules

# 4 :  imports from custom modules

_logger = logging.getLogger(__name__)

class ClientModel(models.Model):
    """ 
    Класс Клиент
    ФИО *
    ФИО родителя 
    Телефон *
    Адрес *
    Дата рождения *
    Дата последнего посещения клуба
    Счетчик пропуска тренировок
    """ 

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'golden_ball.client_model'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------
    name = fields.Char(
        string = "ФИО",
    )

    parents_name = fields.Char(
        string = "ФИО родителя"
    )

    phone_number = fields.Char(
        string = "Номер телефона"
    )

    birthday = fields.Date(
        string = "Дата рождения"
    )

    address = fields.Char(
        string = "Адрес проживания"
    )

    skipping = fields.Integer(
        string = "Количество пропусков"
    )

    date_last_visit = fields.Date(
        string='Дата последней тренировки'
    )

    aboniment_ids = fields.One2many(
        'golden_ball.aboniment_model',
        'aboniment_id',
        string="Абонименты"
    )

    #training_id = fields.Many2one(
    #    'golden_ball.works_model',
    #    string='Тренировка'
   # )

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