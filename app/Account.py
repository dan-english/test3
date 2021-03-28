"""Account Model."""

from masoniteorm.models import Model


class Account(Model):
    """Account Model."""
    __fillable__ = ['email', 'access_token', 'scopes', 'type', 'valid', 'user_id', 'provider', 'nylas_account_id']

    __auth__ = 'email'
