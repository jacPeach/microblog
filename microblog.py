# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:34:18 2020

@author: jacob
"""

from app import db, create_app
from app.models import User, Post

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User":User, "Post":Post}