# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:56:28 2020

@author: jacob
"""

from flask import Blueprint

bp = Blueprint("main", __name__)

from app.main import routes