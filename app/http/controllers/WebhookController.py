"""A NylasController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from app.Account import Account
from app.MessageCategory import MessageCategory
from app.User import User

import requests
import json
from pprint import pprint

class WebhookController(Controller):
    def __init__(self, request: Request):
        self.request = request

    def challenge(self, request:Request):
        challenge = request.input('challenge')
        return challenge

    def message_created(self, request: Request,  auth: Auth):
        print('MESSAGE RECEIVED')
        deltas = request.input('deltas')
        object_data = deltas[0]['object_data']
        pprint(object_data)
        #do something with this
        return []

    def account_invalid(self, request: Request,  auth: Auth):
        print("ACCOUNT INVALID")
        request.session.flash('success', 'Your token is invalid')
        deltas = request.input('deltas')
        # pprint(deltas)
        object_data = deltas[0]['object_data']
        # pprint(object_data)

        account_id = object_data['account_id']
        try:
            users = User.where('nylas_account_id',account_id).get()
            for user in users:
                user.access_token = ''
                user.save()
        except Exception as e:
            print(str(e))

        return []
