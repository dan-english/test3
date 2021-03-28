"""A CRMController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller

from app.http.controllers.NylasController import NylasController
from masonite import Queue
from masonite.auth import Auth
from app.User import User
from app.Deal import Deal
from app.MessageCategory import MessageCategory
import json
from pprint import pprint

from app.http.controllers.PusherController import PusherController



class CRMController(Controller):
    """CRMController Controller Class."""

    def __init__(self, request: Request):
        self.request = request

    def show(self, view: View):
        return view.render('crm.dashboard')

    def show_console(self, view:View):
        return view.render('auth.console')

    def deals(self, view: View):
        return view.render('crm.deals')

    def compose_message(self, view: View):
        return view.render('crm.compose_message')

    def show_inbox(self, request: Request, view: View, auth: Auth):
        return view.render('crm.inbox')

    def show_contacts(self, request: Request, view: View, auth: Auth):
        return view.render('crm.contacts')

    def show_message(self, request: Request, view: View, auth: Auth):
        message_id = request.param('message_id')
        options = {'id':message_id, 'clean':0,}

        return view.render('crm.message', {'data':options})

    def show_message_clean(self, request: Request, view: View, auth: Auth):
        message_id = request.param('message_id')
        options = {'id': message_id,'clean': 1,}

        return view.render('crm.message', {'data':options})


    def get_message_category(self, request: Request, view: View, auth: Auth):
        user_id = auth.user().id
        user = json.loads(User.find(user_id).to_json())
        message_id = request.param('message_id')

        nylasController = NylasController()
        data = nylasController.getMessageCategory(user['access_token'], message_id)

        return data

    def give_message_category_feedback(self, request: Request, view: View, auth: Auth):
        user_id = auth.user().id
        user = json.loads(User.find(user_id).to_json())

        account_id = request.input('account_id')
        message_id = request.input('message_id')

        #
        # nylasController = NylasController()
        # message_category = MessageCategory.where('message_id', message_id).where('account_id', account_id).first()
        #
        # pprint(message_category)

        # result = nylasController.categoryFeedback(postData['message_id'], current_category)

        return []

    ##
    # Get inbox messages for the authenticated use
    ##
    def get_inbox_messages(self, request:Request, auth:Auth):
        user_id = auth.user().id
        user = json.loads(User.find(user_id).to_json())

        nylasController = NylasController()
        messages = nylasController.getMessagesFromInbox(user['access_token'])

        return messages



    def data_get_contacts(self, request: Request, view: View, auth: Auth):
        user_id = auth.user().id
        user = json.loads(User.find(user_id).to_json())
        nylasController = NylasController()
        data = nylasController.getContacts(user['access_token'])

        return data

    def get_deal_leads(self, request: Request,):
        deals = Deal.all()
        return deals
    def get_deal(self, view: View):
        deal = Deal.find(1).to_json()

        return view.render('crm.deal',{
            'data':deal
        })
    def websocket_handler(self, request: Request):
        print("********************* WEBSOCKET HANDLER ************************")

        pc= PusherController()
        pc.text_sendPusherNotification('websocket_handler')

        return []



    def data_get_message_clean(self, request: Request, view: View, auth: Auth):
        user_id = auth.user().id
        user = json.loads(User.find(user_id).to_json())
        message_id = request.param('message_id')
        nylasController = NylasController()
        data = nylasController.getCleanMessage(user['access_token'], [message_id])
        pprint(data)

        return data


    def data_get_thread(self, request: Request, view: View, auth: Auth):
        user_id = auth.user().id
        user = json.loads(User.find(user_id).to_json())
        message_id = request.param('message_id')
        nylasController = NylasController()
        data = nylasController.getMessagesForThread(user['access_token'], message_id)

        return data
    def data_get_thread_clean(self, request: Request, view: View, auth: Auth):
        user_id = auth.user().id
        user = json.loads(User.find(user_id).to_json())
        message_id = request.param('message_id')
        nylasController = NylasController()
        # data = nylasController.getCleanMessage(user['access_token'], [message_id]) //this was for the demo panel
        data = nylasController.getMessagesCleanedForThread(user['access_token'], message_id)


        return data



    def data_message_signature(self, request: Request, view: View, auth: Auth):
        user_id = auth.user().id
        user = json.loads(User.find(user_id).to_json())
        message_id = request.param('message_id')

        nylasController = NylasController()
        data = nylasController.getMessageSignature(user['access_token'], message_id)

        return data
