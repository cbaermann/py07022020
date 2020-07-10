from __future__ import unicode_literals
from django.db import models
import bcrypt
from validate_email import validate_email

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name should be at least 2 characters."

        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be at least 2 characters."

        if not validate_email(postData["email"]):
            errors["email"] = "Invalid email address"
        if User.objects.filter(email = postData["email"]):
            errors["inUserEmail"] = "Email address already in use"

        if len(postData["password"]) < 8:
            errors["password_length"] = "Password must be at least 8 characters."
        if postData["password"] != postData["confirm"]:
            errors["password"] = "Passwords do not match"

        return errors
    def login_validator(self, postData):
        errors = {}
        try : 
            user = User.objects.get(email = postData["email"])
        except:
            errors["email"] = f"No email adress matching {postData['email']}"
            return errors

        if not bcrypt.checkpw(postData["password"].encode(), user.password.encode()):
            errors["password"] = "Password does not match email"
        return errors
class EventManager(models.Manager):
    def event_validator(self, postData):
        errors = {}

        if len(postData["title"]) < 4:
            errors["title"] = "Title must be 3 characters long"
        if len(postData["genre"]) <1:
            errors["genre"] = "Event must have a genre"

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"<User object: {self.first_name} ({self.last_name})>"

class Event(models.Model):
    title = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)
    date = models.DateTimeField()
    genre = models.CharField(max_length=255)
    attendent = models.ManyToManyField(User, related_name = "attendent")
    creator = models.ForeignKey(User, related_name = "creator")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EventManager()

    def __repr__(self):
        return f"<Event object: {self.title} ({self.location})>"


    

