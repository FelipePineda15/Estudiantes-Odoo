# -*- coding: utf-8 -*-

from openerp import models, fields

class estudiantes(models.Model):
    _name = 'estudiantes.estudiantes'
    name= fields.Many2one('res.partner', string='Nombre', required = True)
    materia= fields.Many2one('materia.materia', string = 'Materia', required = True)
    nota= fields.Float('Nota', required = True)

class materia(models.Model):
    _name = 'materia.materia'
    name = fields.Char('Materia', required = True)

class herencia(models.Model):
    _inherit = 'res.partner'
    materias_ids = fields.One2many('estudiantes.estudiantes','name', string = 'Materia')