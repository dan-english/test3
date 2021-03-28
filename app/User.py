"""User Model."""

from masoniteorm.models import Model


class User(Model):
    """User Model."""

    __fillable__ = ['name', 'email', 'password', 'language','currency', 'access_token', 'enabled','mobile_number','avatar','time_zone','open_hours', 'connected_email', 'connected_calendar', 'nylas_account_id']

    __auth__ = "email"
