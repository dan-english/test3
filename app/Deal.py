"""Deal Model."""

from masoniteorm.models import Model


class Deal(Model):
    """Deal Model."""
    __fillable__ = ['user_id','title', 'description', 'organisation', 'contact','owner','stage','wom','value', 'estimated_close_date']

    __auth__ = 'email'
