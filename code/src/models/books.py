from pydoc import describe
from flask_restx import fields

from src.server.instance import server

book = server.api.model('Book', {
    'valor': fields.Integer(),
    'title': fields.String()
})