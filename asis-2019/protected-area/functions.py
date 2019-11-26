from flask import request, abort
from functools import wraps
import traceback, os, hashlib
from config import *

def check_login(f):
    """
    Wraps routing functions that require a user to be logged in
    """
    @wraps(f)
    def wrapper(*args, **kwds):
        try:
            ah = request.headers.get('ah')

            if ah == hashlib.md5((Config.ADMIN_PASS + Config.SECRET).encode("utf-8")).hexdigest():
                return f(*args, **kwds)
            else:
                return abort(403)

        except:
            return abort(403)
        
    return wrapper

    