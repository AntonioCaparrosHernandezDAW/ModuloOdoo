{
    'name': "Libros",
    'summary': "Gestor de Libros",
    'description': "Módulo para administrar libros de texto.",
    'author': "Antonio Caparrós Hernández",
    'website': "https://AntonioWebs.com",
    'category': 'Sales',
    'version': '1.0',
    'application': True, 
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/vistaLibros.xml',
        'views/viewEtiquetas.xml'
    ],
    'installable': True,
    'auto_install': False,
    'image': '/ProyectoLibros/static/description/logo.png'
}
