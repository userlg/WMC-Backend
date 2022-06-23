from flask_mongoengine import mongoengine as me, BaseQuerySet

from werkzeug.security import check_password_hash,generate_password_hash

from datetime import datetime as dt

class User(me.Document):
    username = me.StringField(required=True, unique=True, trim=True)
    year = me.IntField()
    create_at = me.DateTimeField(default=dt.now())
    
    #Meta Tag is to work with the mongoengine
    meta = { 'collection': 'users', 'queryset_class': BaseQuerySet}
 

'''
    rated = me.StringField()
    director = me.StringField()
    actors = me.ListField()

    from flask_mongoengine import mongoengine as me, BaseQuerySet
    from flask import jsonify
    from werkzeug.security import check_password_hash,generate_password_hash
    import datetime



class User(me.Document):
    #id = me.IntField(autoincrement=True,primary_key=True)
    username = me.StringField(required=True,trim=True,unique=True)
    password = me.StringField(required=True)
    create_at = me.DateTimeField(required=True,default=datetime.datetime.now())

    meta = { 'collection': 'users', 'queryset_class': BaseQuerySet}
   
'''