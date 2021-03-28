"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),
    Get('/callback', 'NylasController@oauthcallback'),

]

PROFILE_ROUTES = [
    Get('/profile', 'ProfileController@show').name('profile').middleware('auth'),
    Post('/avatar', 'ProfileController@saveavatar').name('avatar').middleware('auth'),


    Get('/profile/details', 'ProfileController@getPersonaldetails').name('email_accounts').middleware('auth'),
    Post('/profile/update', 'ProfileController@updateUserDetails').name('profile_update').middleware('auth'),
    Post('/profile/update/openhours', 'ProfileController@updateUserOpenHours').name('profile_update_open_hours').middleware('auth'),

    Get('/accounts/email', 'ProfileController@getEmailAccounts').name('email_accounts').middleware('auth'),
    Get('/accounts/calendar', 'ProfileController@getCalendarAccounts').name('cal_accounts').middleware('auth'),
    Get('/accounts/contact', 'ProfileController@getContactAccounts').name('contact_accounts').middleware('auth'),
    Post('/accounts/delete', 'ProfileController@deleteAccount').name('delete_account').middleware('auth'),

    Post('/demo-data/accounts', 'ProfileController@createDemoAccounts').name('demo_accounts').middleware('auth'),


]
WEBHOOK_ROUTES=[
    # Get('/webhook/account/invalid', 'WebhookController@challenge').name('challenge'),

    Post('/webhook/account/invalid', 'WebhookController@account_invalid').name('account_invalid'),
    Post('/webhook/message/created', 'WebhookController@message_created').name('message_created')

]
CONTACTS_ROUTES=[
    Get('/contacts', 'CRMController@show_contacts').name('contacts').middleware('auth'),
    Get('/data/contacts', 'CRMController@data_get_contacts').name('data_get_contacts').middleware('auth'),

]

EMAIL_ROUTES = [
    Get('/inbox', 'CRMController@show_inbox').name('inbox').middleware('auth'),
    Get('/inbox/message/@message_id', 'CRMController@show_message').name('message'),
    Get('/inbox/message/clean/@message_id', 'CRMController@show_message_clean').name('message'),
    Get('/inbox/messages', 'CRMController@get_inbox_messages').name('message'),

    Get('/message/category/@message_id', 'CRMController@get_message_category').name('category'),
    Get('/message/signature/@message_id', 'CRMController@data_message_signature').name('signature'),
    Get('/message/clean/@message_id', 'CRMController@data_get_message_clean').name('message'),

    Post('/message/category/feedback', 'CRMController@give_message_category_feedback').name('category_feedback'),

    Get('/compose', 'CRMController@compose_message').name('compose'),

    Get('/data/message/clean/@message_id', 'CRMController@data_get_message_clean').name('compose'),

    Get('/data/inbox/thread/@message_id', 'CRMController@data_get_thread').name('compose'),
    Get('/data/inbox/thread/clean/@message_id', 'CRMController@data_get_thread_clean').name('compose'),
]



DEALS_ROUTES = [
    Get('/deals', 'CRMController@deals').name('deals').middleware('auth'),
    Get('/deals/leads', 'CRMController@get_deal_leads').name('deals_leads').middleware('auth'),
    Get('/deal/@deal_id', 'CRMController@get_deal').name('deals_summary').middleware('auth'),
]

WEBSOCKET_ROUTES = [
    Post('/websocket', 'CRMController@websocket_handler'),
]

CRM_ROUTES = [
    Get('/crm', 'CRMController@show').name('crm_dashboard').middleware('auth'),
    Get('/console', 'CRMController@show_console').name('console').middleware('auth'),

]
from masonite.auth import Auth
ROUTES += Auth.routes()
ROUTES += PROFILE_ROUTES
ROUTES += CRM_ROUTES
ROUTES += EMAIL_ROUTES
ROUTES += DEALS_ROUTES
ROUTES += WEBSOCKET_ROUTES
ROUTES+=CONTACTS_ROUTES
ROUTES+=WEBHOOK_ROUTES
