from odoo import models, fields # type: ignore

class Libro(models.Model):
    _name = 'libro'
    _description = 'Modelo de Libro'

    name = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor', required=True)
    fecha_publicacion = fields.Date(string='Fecha de Publicación')
    isbn = fields.Char(string='ISBN', unique=True)
    paginas = fields.Integer(string='Número de Páginas')
    editorial = fields.Char(string='Editorial', required=True, default="Sin editorial")
    disponible = fields.Boolean(string='Disponible', default=True)
    imagen = fields.Image(string='Imagen de Libro')
    etiquetas = fields.Many2many('etiquetas.model', string="Etiquetas")


class Etiqueta(models.Model):
    _name = "etiquetas.model"
    _description = "Etiquetas para propiedades"

    name = fields.Char("Nombre", required=True)
    color = fields.Integer("Color")
