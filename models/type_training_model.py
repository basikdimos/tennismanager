# -*- coding: utf-8 -*-

# 1 : imports of python lib
import logging

# 2 :  imports of odoo
from odoo import api, fields, models

# 3 :  imports of odoo modules

# 4 :  imports from custom modules

_logger = logging.getLogger(__name__)

class GoldenballTypeTraining(models.Model):
    """ 
    Тип треннировки
    """ 

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'golden_ball.type_training_model'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------
    name = fields.Char(
        string='Наименовние',
        required=True
    )

    number_people = fields.Integer(
        string='Количество людей'
    )

    client_ids = fields.Many2many(
        'golden_ball.client_model',
        #'training_id',
        string='Клиенты',
    )

    type_aboniment = fields.Many2one(
        'golden_ball.aboniment_type_model',
        string='Тип абонимента'
    )

    creator_work = fields.Char(
        string='Создал:',
        default=""
    )

    editor_work = fields.Char(
        string='Изменел:',
        default=""
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
    @api.model
    def create(self, vals):
        res = super(GoldenballTypeTraining, self).create(vals)
        creator = self.env['res.users'].search(
            [('id', '=', res.create_uid.id)]
        ).display_name
        res.creator_work = creator
        return res

    @api.multi
    def write(self, vals):
        #writer = vals.get('write_uid')
        writer_name = self.env['res.users'].search(
            [('id', '=', self.write_uid.id)]
        ).display_name
        vals['editor_work'] = writer_name
        res = super(GoldenballTypeTraining, self).write(vals)
        return res