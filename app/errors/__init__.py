# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 14:35:42 2020

@author: jacob
"""

from flask import Blueprint

bp = Blueprint("errors", __name__, template_folder="templates")

from app.errors import handlers