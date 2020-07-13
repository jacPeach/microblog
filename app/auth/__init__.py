# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 14:46:00 2020

@author: jacob
"""

from flask import Blueprint

bp = Blueprint("auth", __name__, template_folder="templates")

from app.auth import routes