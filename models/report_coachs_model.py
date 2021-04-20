# -*- coding: utf-8 -*-

# 1 : imports of python lib
import logging

# 2 :  imports of odoo
from odoo import api, fields, models, tools

# 3 :  imports of odoo modules

# 4 :  imports from custom modules

_logger = logging.getLogger(__name__)

class CoachReport(models.Model):
    """ 
    Отчет по тренерам
    """ 

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'golden_ball.report_coachs_model'
    _auto = False

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------
    coach = fields.Char(
        string='Тренер'
    )

    trainig_type = fields.Many2one(
        'golden_ball.type_training_model',
        string='Тип треннировки',
        required=True
    )

    date_workout = fields.Datetime(
        string='Дата тренировки'
    )

    month_workout = fields.Integer(
        string="Номер месяца"
    )

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------

    # Action methods
    # ------------------------------------------------------------------------------------------------------------------
    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'golden_ball_report_coachs_model')
        self.env.cr.execute(
            """
            CREATE OR REPLACE VIEW golden_ball_report_coachs_model AS(
            WITH tmp_golden_ball_report_coachs_model AS(
            SELECT
            works.id AS id,
            CASE
                WHEN (works.coach_id<>0) THEN 
                    (
                        SELECT name
                        FROM golden_ball_coach_model AS coach_name
                        WHERE coach_name.id = works.coach_id
                    )
                ELSE 'Аренда'
            END AS coach,
            works.name AS trainig_type,
            works.date_workout AS date_workout
            FROM golden_ball_works_model AS works
            )
            SELECT * 
            FROM tmp_golden_ball_report_coachs_model
            )
            """
        )

    """

            EXTRACT(MONTH FROM works.date_workout) AS month_workout


    SELECT * 
            FROM tmp_golden_ball_report_coachs_model
            WHERE tmp_golden_ball_report_coachs_model.month_workout = EXTRACT(month FROM now())
    """
    # Business methods
    # ------------------------------------------------------------------------------------------------------------------


    # CRUD methods
    # ------------------------------------------------------------------------------------------------------------------