"""A NylasController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from app.Account import Account
from app.MessageCategory import MessageCategory

from app.http.controllers.PusherController import PusherController

import requests
import json
from pprint import pprint

class NylasController(Controller):
    """NylasController Controller Class."""

    def __init__(self):
        """NylasController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.apiUrl   = "https://api.nylas.com"
        self.pusher = PusherController()


    def oauthcallback(self, view: View, request: Request, auth: Auth):

        nylas_access_token = request.input('access_token')
        nylas_account_id = request.input('account_id')
        email_address = request.input('email_address')
        provider = request.input('provider')
        # a cookie is set so we can identify where the user started the auth process
        start_page_type = request.get_cookie('callbackpage', decrypt=False)

        user = auth.user()

        #we want to treat this as a master token so it doesnt change when auth'ing with different scopes
        if start_page_type == 'connect_personal':
            user.access_token = nylas_access_token
            user.nylas_account_id = nylas_account_id
            user.save()

        try:
            Account.update_or_create({"user_id": user.id, "nylas_account_id": nylas_account_id,"type":start_page_type }, {
                    "access_token": nylas_access_token,
                    "email":email_address,
                    "nylas_account_id": nylas_account_id,
                    "type": start_page_type,
                    "scopes": start_page_type,
                    "provider":provider,
                    "valid":1
            })
        except Exception as e:
            print(str(e))


        return view.render('auth.callback', {
            'email_address': email_address,
            'provider': provider,
            'nylas_access_token': nylas_access_token,
            'nylas_account_id': nylas_account_id
        })

    def getAccountDetails(self, access_token):
        url = self.apiUrl + '/account'
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        try:
            response = requests.request('GET', url, headers=headers)
            account_details = json.loads(response.text)
        except Exception as e:
            print(str(e))

        return account_details


    def getMessages(self, access_token):
        url = self.apiUrl + '/messages'


        headers  = {'authorization': access_token, 'content-type': 'application/json'}
        data =[]
        try:
            response = requests.request('GET', url, headers=headers)
            messages = json.loads(response.text)
            jr = self.buildJsonRequest('GET', response)
            self.pusher.sendPusherNotification(jr)
            for message in messages:
                data.append( {
                    'id':message['id'],
                    'to':message['to'],
                    'from': message['from'],

                    'started':message['starred'],
                    'unread':message['unread'],
                    'date':message['date'],
                    'snippet':message['snippet'],
                    'subject':message['subject']
                    #whos lead it is
                    #shared?
                    #attachements

                })



        except Exception as e:
            print(str(e))

        return json.dumps(data)

    def getMessagesFromInbox(self, access_token):
        url = self.apiUrl + '/messages?in=inbox'
        headers  = {'authorization': access_token, 'content-type': 'application/json'}

        data =[]
        try:
            response = requests.request('GET', url, headers=headers)

            jr=self.buildJsonRequest('GET', response)
            self.pusher.sendPusherNotification(jr)

            messages = json.loads(response.text)




            for message in messages:

                message_category = MessageCategory.where('message_id', message['id']).first()

                if message_category is not None:
                    category = message_category.category
                else:
                    category = ''


                data.append( {
                    'id':message['id'],
                    'to':message['to'],
                    'from': message['from'],

                    'starred':message['starred'],
                    'unread':message['unread'],
                    'date':message['date'],
                    'snippet':message['snippet'],
                    'subject':message['subject'],
                    'files':message['files'],
                    'category':category
                    #whos lead it is
                    #shared?
                    #attachements

                })

        except Exception as e:
            print(str(e))

        return data

    def getMessage(self, access_token, message_id):
        url = self.apiUrl + '/messages/'+message_id
        headers  = {'authorization': access_token, 'content-type': 'application/json'}
        message = {}
        try:
            response = requests.request('GET', url, headers=headers)
            #
            jr=self.buildJsonRequest('GET', response)
            self.pusher.sendPusherNotification(jr)

            message = json.loads(response.text)
        except Exception as e:
            print(str(e))

        return message

    def getCleanMessage(self, access_token, message_ids):
        url = self.apiUrl + '/neural/conversation'

        headers = {'authorization': access_token, 'content-type': 'application/json'}
        message={}
        data = {
            'message_id':message_ids,
            "ignore_links": True,
            "ignore_images": True,
            'ignore_tables': True,
            'remove_conclusion_phrases':True,
            'images_as_markdown':False,
        }
        try:
            response = requests.request('PUT', url,  data=json.dumps(data),  headers=headers)
            jr = self.buildJsonRequest('PUT', response)
            self.pusher.sendPusherNotification(jr)

            message = json.loads(response.text)
        except Exception as e:
            print(str(e))

        return message

    def getThread(self, access_token, thread_id):
        url = self.apiUrl + '/threads/' + thread_id
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        thread = {}
        try:
            response = requests.request('GET', url, headers=headers)
            jr = self.buildJsonRequest('GET', response)
            self.pusher.sendPusherNotification(jr)
            thread = json.loads(response.text)
        except Exception as e:
            print(str(e))

        return thread

    def getMessagesForThread(self, access_token, message_id):

        url = self.apiUrl + '/messages?in=inbox'
        message = self.getMessage(access_token, message_id)
        thread = self.getThread(access_token, message['thread_id'])

        messages = []
        messages.append(message)
        for thread_message_id in thread['message_ids']:
            if thread_message_id != message_id:
                print('we should get this message')

                thread_message = self.getMessage(access_token, thread_message_id)
                messages.append(thread_message)


        thread['messages'] = messages
        thread['display_message'] = message_id
        return json.dumps(thread)

    def getMessagesCleanedForThread(self, access_token, message_id):

        url = self.apiUrl + '/messages?in=inbox'
        message = self.getMessage(access_token, message_id)

        thread = self.getThread(access_token, message['thread_id'])
        cleaned_messages = self.getCleanMessage(access_token, thread['message_ids'])

        thread['messages'] = cleaned_messages
        thread['display_message'] = message_id

        return json.dumps(thread)



    ## Get the category for one message
    def getMessageCategory(self, access_token, message_id):

        url = self.apiUrl + '/neural/categorize'
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data = {
            'message_id': [message_id],
            'only_category':True
        }
        message=''
        try:
            response = requests.request('PUT', url, data=json.dumps(data), headers=headers)
            jr = self.buildJsonRequest('GET', response)
            self.pusher.sendPusherNotification(jr)
            messages = json.loads(response.text)
            message = messages[0]

            try:
                MessageCategory.update_or_create({"message_id": message['id'], "account_id": message['account_id']}, {
                    "category": message['category'],
                    "model_version": message['model_version'],
                    "categorized_at": message['categorized_at']
                })
            except Exception as e:
                print(str(e))

        except Exception as e:
            print(str(e))

        return message['category']

    ## Get the category for multiple messages
    def getMessagesCategory(self, access_token, message_ids):

        url = self.apiUrl + '/neural/categorize'
        headers = {'authorization': access_token, 'content-type': 'application/json'}

        a = message_ids[:5]
        data = {
            'message_id': a,
            'only_category':True
        }


        messages=[]
        try:
            response = requests.request('PUT', url, data=json.dumps(data), headers=headers)
            messages = json.loads(response.text)

            ## update the table for message category mapping. this is persistant so anyone who uses the same account will already have these cached
            for message in messages:
                try:
                    MessageCategory.update_or_create({"message_id":message['id'], "account_id":message['account_id'] }, {
                     "category" : message['category'],
                     "model_version" : message['model_version'],
                     "categorized_at" : message['categorized_at']
                    })
                except Exception as e:
                    print(str(e))
        except Exception as e:
            print(str(e))

        return messages


    def categoryFeedback(self):
        return []


    def getMessageSignature(self, access_token, message_id):

        url = self.apiUrl + '/neural/signature'
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        data = {
            'message_id': [message_id],
            "ignore_links": True,
            "ignore_images": True,
            "ignore_tables": False,
            "remove_conclusion_phrases": True,
            "images_as_markdown": False,
            "parse_contacts": True
        }
        signature=''
        try:
            response = requests.request('PUT', url, data=json.dumps(data), headers=headers)
            jr = self.buildJsonRequest('GET', response)
            self.pusher.sendPusherNotification(jr)
            message = json.loads(response.text)
            signature = message[0]

        except Exception as e:
            print(str(e))

        return signature




    def getContacts(self, access_token):
        url = self.apiUrl + '/contacts'
        headers = {'authorization': access_token, 'content-type': 'application/json'}
        contacts = []
        try:
            response = requests.request('GET', url, headers=headers)
            #
            jr = self.buildJsonRequest('GET', response)
            self.pusher.sendPusherNotification(jr)

            contacts = json.loads(response.text)
        except Exception as e:
            print(str(e))

        return contacts








    def buildJsonRequest(self, method, response):
      return {
            "method": method,
            "url": response.url,
            "status": response.status_code,
            "content-type": response.headers['content-type'],
            "elapsed": "0.05",
            "type":"API Request",
            "received":response.text
        }




