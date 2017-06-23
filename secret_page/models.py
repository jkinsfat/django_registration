# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
import re

def validate_word(value):
    if len(value) < 2:
        raise ValidationError('Field must be longer than one character')
    pattern = re.compile("[A-Za-z]+$")
    match = pattern.match(value)
    if not match:
        raise ValidationError('Field must contain only letters')

def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Password must be longer than 8 characters')

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25, validators=[validate_word])
    last_name = models.CharField(max_length=25, validators=[validate_word])
    email = models.CharField(max_length=25, unique=True, validators=[validate_email])
    password = models.CharField(max_length=25, validators=[validate_password])
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

class Secret(models.Model):
    secret = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    secret = models.ForeignKey(Secret, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank = True)
    updated_at = models.DateTimeField(auto_now_add=True, blank = True)
