from flask import Flask
from flask_restx import Api, Resource
from pymongo import MongoClient

from src.server.instance import server
from src.models.books import book

app, api = server.app, server.api
client = MongoClient('mongodb://admin:pass@mongo-dev')

db = client.book
collection = db.books

@api.route('/books')
class BookList(Resource):
    @api.marshal_list_with(book)
    def get(self):
        books = collection.find({})
        return list(books)
    @api.expect(book, validate=True)
    def post(self):
        #import ipdb; ipdb.set_trace()
        response = api.payload
        collection.insert_one(response)
        response.pop('_id')
        return response, 200