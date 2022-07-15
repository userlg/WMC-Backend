from flask_mongoengine import mongoengine as me, BaseQuerySet

from datetime import datetime as dt

class Blacklist(me.Document):
    jwt = me.StringField(required=True, unique=True)
    id_user = me.IntField(required=True)
    create_at = me.DateTimeField(default=dt.now())
    
    #Meta Tag is to work with the mongoengine
    meta = { 'collection': 'blacklist', 'queryset_class': BaseQuerySet}