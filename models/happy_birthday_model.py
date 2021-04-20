# -*- coding: utf-8 -*-

# 1 : imports of python lib
import logging

# 2 :  imports of odoo
from odoo import api, fields, models, tools

# 3 :  imports of odoo modules

# 4 :  imports from custom modules

_logger = logging.getLogger(__name__)

class HappyBDay(models.Model):
    """ 
    Description
    """ 

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'golden_ball.bday_model'
    _auto = False

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------
    name = fields.Char(
        string = "ФИО",
    )

    phone_number = fields.Char(
        string = "Номер телефона"
    )

    birthday = fields.Date(
        string = "Дата рождения"
    )

    date_last_visit = fields.Date(
        string='Последнее посещение'
    )

    month_bday = fields.Integer(
        string="Номер месяца"
    )

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------

    # Action methods
    # ------------------------------------------------------------------------------------------------------------------
    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'golden_ball_bday_model')
        self.env.cr.execute(
            """
            CREATE OR REPLACE VIEW golden_ball_bday_model AS(
            WITH tmp_golden_ball_bday_model AS (
            SELECT
            clients.id AS id,
            clients.name AS name,
            clients.phone_number AS phone_number,
            clients.birthday AS birthday,
            EXTRACT(MONTH FROM clients.birthday) AS month_bday,
            clients.date_last_visit AS date_last_visit
            FROM golden_ball_client_model AS clients
            )
            SELECT *
            FROM tmp_golden_ball_bday_model
            WHERE tmp_golden_ball_bday_model.month_bday = EXTRACT(month FROM now())
            )
            """
        )

    # Business methods
    # ------------------------------------------------------------------------------------------------------------------

    # CRUD methods
    # ------------------------------------------------------------------------------------------------------------------