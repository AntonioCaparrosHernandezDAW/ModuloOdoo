from odoo import models, fields  # type: ignore

class Etiqueta_Model(models.Model):
    _name = "etiqueta.model"
    _description = "Etiquetas para clasificar géneros de libros"

    name = fields.Char("Etiqueta", required=True)
    color = fields.Integer("Color")
