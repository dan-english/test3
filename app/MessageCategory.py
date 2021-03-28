"""MessageCategory Model."""

from masoniteorm.models import Model


class MessageCategory(Model):
    """MessageCategory Model."""
    __table__ = 'message_category'

    __fillable__ = ['account_id','message_id', 'category', 'model_version', 'categorized_at']

    __auth__ = 'email'
