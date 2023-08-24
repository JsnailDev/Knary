#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Descripttion: https://github.com/JsnailDev/Knary
# version: 0.0.1
# Author: Joseph NOMO (fulgaros@gmail.com)
# Create: 2023-08-20 18:37:23
# LastAuthor: Joseph NOMO
# lastTime: 2023-08-20 18:37:23
# --------------------------------------------------------
import datetime
from peewee import *
from app.db.database import BaseModel


# define all database tables
# 用户
class Users(BaseModel):
    id = AutoField()
    user_id = CharField(unique=True)
    username = CharField()
    user_phone = CharField()
    email = CharField()
    salt = CharField()
    hashed_password = CharField()
    bio = CharField(default="你好")
    image = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
