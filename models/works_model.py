# -*- coding: utf-8 -*-

# 1 : imports of python lib
import logging, datetime

# 2 :  imports of odoo
from odoo import api, fields, models

# 3 :  imports of odoo modules

# 4 :  imports from custom modules

_logger = logging.getLogger(__name__)

class GoldenballWorks(models.Model):
    """ 
    Description
    """ 

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'golden_ball.works_model'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------
    name = fields.Many2one(
        'golden_ball.type_training_model',
        string='Тип треннировки',
        required=True
    )

    client_ids = fields.Many2many(
        'golden_ball.client_model',
        #'training_id',
        string='Клиенты',
    ) 

    date_workout = fields.Datetime(
        string='Дата тренировки'
    )

    coach_id = fields.Many2one(
        'golden_ball.coach_model',
        string='Тренер'
    )

    cort_id = fields.Many2one(
        'golden_ball.cort_number_model',
        string='Корт'
    )

    is_done = fields.Boolean(
        string="Проведена?"
    )

    #creator_work = fields.Char(
    #   string='Создал:',
    #    default=" "
    #)

    #editor_work = fields.Char(
    #    string='Изменел:',
    #    default=" "
   # )

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------
    @api.onchange('name')
    def _onchange_type_training(self):
        clients = self.env['golden_ball.type_training_model'].search(
            [('id', '=', self.name.id)]
        )
        self.client_ids = clients.client_ids


    #@api.onchange('date_workout')
    #def _onchange_date_workout(self):
    #    if (self.client_ids):
    #        clients = self.env['golden_ball.client_model'].search(
    #            [('id', '=', self.client_ids.id)]
    #        )
    #        for record in clients:
    #            record.date_last_workout = self.date_workout
        
    # Action methods
    # ------------------------------------------------------------------------------------------------------------------
    @api.multi
    def action_done(self):
        self.is_done = True
        client_ids = self.client_ids
        #str_time = self.date_workout.to_string()
        #dt = datetime.datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
        #dd = dt.date()
        for records in client_ids:
            clients = self.env['golden_ball.client_model'].search(
                [('id', '=', records.id)]
            )
            for record in clients:
                abon_ids = record.aboniment_ids
                #if (record.date_last_visit == False):
                #   aboniments = self.env['golden_ball.aboniment_model'].search(
                #        [('id', '=', record.aboniment_ids.id)]
                #    )
                #    aboniments.date_begin = (self.date_workout).date()
                aboniment = self.env['golden_ball.aboniment_model'].search(
                    [('id', '=', abon_ids.id)]
                )
                for vals in aboniment:
                    vals.date_begin = (self.date_workout).date()
                record.date_last_visit = (self.date_workout).date()

    # Business methods
    # ------------------------------------------------------------------------------------------------------------------

    # CRUD methods
    # ------------------------------------------------------------------------------------------------------------------
    #@api.model
    #def create(self, vals):
    #   res = super(GoldenballWorks, self).create(vals)
    #    creator = self.env['res.users'].search(
    #        [('id', '=', res.create_uid.id)]
    #    ).display_name
    #    res.creator_work = creator
    #    return res

    #@api.model
    #def create(self, vals):
    #  res = super().create(vals)
    #    date_workout = res.date_workout
    #    client_ids = res.client_ids
    #   for records in client_ids:
    #        clients = self.env['golden_ball.client_model'].search(
    #            [('id', '=', records.id)]
    #        )
    #        for record in clients:
    #            if (date_workout < record.date_last_workout):
    #                record.date_last_workout = date_workout
    #    return res

    #@api.multi
    #def write(self, vals):
    #   writer_name = self.env['res.users'].search(
    #       [('id', '=', self.env.uid)]
    #    ).display_name
    #    vals['editor_work'] = writer_name
    #    res = super(GoldenballWorks, self).write(vals)
    #    return res

    #@api.multi
    #def write(self, vals):
    #    date_workout = vals.get('date_workout')
    #    client_ids = self.client_ids
    #    for records in client_ids:
    #        clients = self.env['golden_ball.client_model'].search(
    #            [('id', '=', records.id)]
    #        )
    #        for record in clients:
    #            if (date_workout < record.date_last_workout):
    #                record.date_last_workout = date_workout
    #    res = super().write(vals)
    #    return res
    
    #@api.multi
    #def unlink(self):
    #    clients = self.env['golden_ball.client_model'].search(
    #        [('id', '=', self.client_ids.id)]
    #    )
    #    for record in clients:
    #        record.date_last_workout = ''
    #  return super(GoldenballWorks, self).unlink()