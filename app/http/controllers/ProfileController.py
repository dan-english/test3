"""A ProfileController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from app.User import User
from masonite import Upload
from app.Account import Account
import random
from pprint import pprint
import json

class ProfileController(Controller):
    """ProfileController Controller Class."""

    def __init__(self, request: Request):
        """ProfileController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, request: Request, view: View, auth: Auth):

        authed_id = auth.user().id
        user = json.loads(User.find(authed_id).to_json())

        del user['verified_at']

        if user['open_hours'] is None or user['open_hours'] == '':
            user['open_hours'] = {}
        else:
            user['open_hours'] = json.loads(user['open_hours'])

        user['validToken'] = self.tokenCheck()

        return view.render('auth.profile', {
            'data': user,
        })


    def updateUserDetails(self, request:Request, auth:Auth):
        postData = request.input('user_data')
        user_id =  auth.user().id
        user = User.find(user_id)

        try:
            user.name = postData['name']
            user.access_token = postData['access_token']
            user.time_zone = postData['time_zone']
            user.mobile_number = postData['mobile_number']
            user.avatar = postData['avatar']
            user.currency = postData['currency']
            user.language = postData['language']

            pprint(user)

            user.save()
        except Exception as e:
            print(str(e))
            return 0

        return 1

    def updateUserOpenHours(self, request: Request, auth:Auth):

        postData = request.input('user_data')
        user_id = auth.user().id
        user = User.find(user_id)

        try:
            user.open_hours = json.dumps(postData['open_hours'])
            user.save()
        except Exception as e:
            print(str(e))
            return 0

        return 1

    def saveavatar(self, request:Request, upload: Upload):
        try:
            filename = upload.driver('disk').store(request.input('file'))
            return filename
        except Exception as e:
            print(str(e))
            return 0

    #check if the token is active, may not need this anymore if the webhook is running
    def tokenCheck(self):
        return 1


    def getPersonaldetails(self,request:Request, auth:Auth):
        authed_id = auth.user().id
        user = json.loads(User.find(authed_id).to_json())
        if user['open_hours'] is None or user['open_hours'] == '':
            user['open_hours'] = {}
        else:
            user['open_hours'] = json.loads(user['open_hours'])

        return user

    def getEmailAccounts(self, request:Request, auth:Auth):
        authed_id = auth.user().id
        user = User.find(authed_id)
        email_accounts = Account.where('user_id', user.id).where('type', 'connect_email').get()
        if email_accounts != None:
            return email_accounts

        return []
    def getCalendarAccounts(self, request:Request, auth:Auth):
        authed_id = auth.user().id
        user = User.find(authed_id)
        email_accounts = Account.where('user_id', user.id).where('type', 'connect_calendar').get()
        if email_accounts != None:
            return email_accounts

        return []
    def getContactAccounts(self, request:Request, auth:Auth):
        authed_id = auth.user().id
        user = User.find(authed_id)

        email_accounts = Account.where('user_id', user.id).where('type', 'connect_contact').get()
        if email_accounts != None:
            return email_accounts

        return []


    def deleteAccount(self, request:Request, auth:Auth):
        authed_id = auth.user().id
        postData = request.input('data')
        account_id = postData['id']

        try:
            pprint(account_id)
            account = Account.where('user_id', authed_id).where('id',account_id).first()
            account.delete()
            return 1
        except Exception as e:
            print(str(e))
            return 0



## DEMO DATA
    def createDemoAccounts(self, request:Request, auth:Auth):
        user_id = auth.user().id
        name = request.input('name')
        if name == "":
            return 0

        providers = [
                    'outlook',
                    'apple',
                    'gmail',
                    'yahoo',
                    'office365'
                    ]

        for provider in providers:
            fake_email = name + '@' + provider + '.com'
            type='connect_email'
            # check if this type of connection has been completed before by the email address
            the_account = Account.where('user_id', user_id).where('email', fake_email).where('type', type).first()

            if the_account is None:
                account = Account()
                account.user_id = user_id
                account.access_token = 'demo_so_doesnt_matter'
                account.email = fake_email
                account.provider = provider
                account.nylas_account_id = 'demo_so_doesnt_matter'
                account.scopes = 'demo_so_doesnt_matter'
                account.type = type
                account.valid = bool(random.getrandbits(1))
                account.save()

        for provider in providers:
            fake_email = name + '@' + provider + '.com'
            type = 'connect_calendar'
            the_account = Account.where('user_id', user_id).where('email', fake_email).where('type', type).first()

            if provider == 'yahoo':
                continue

            if the_account is None:
                account = Account()
                account.user_id = user_id
                account.access_token = 'demo_so_doesnt_matter'
                account.email = fake_email
                account.provider = provider
                account.nylas_account_id = 'demo_so_doesnt_matter'
                account.scopes = 'demo_so_doesnt_matter'
                account.type = type
                account.valid = bool(random.getrandbits(1))
                account.save()
        #
        for provider in providers:

            fake_email = name + '@' + provider + '.com'
            type = 'connect_contact'
            the_account = Account.where('user_id', user_id).where('email', fake_email).where('type', type).first()

            if the_account is None:
                account = Account()
                account.user_id = user_id
                account.access_token = 'demo_so_doesnt_matter'
                account.email = fake_email
                account.provider = provider
                account.nylas_account_id = 'demo_so_doesnt_matter'
                account.scopes = 'demo_so_doesnt_matter'
                account.type = type
                account.valid = bool(random.getrandbits(1))
                account.save()

        return True
