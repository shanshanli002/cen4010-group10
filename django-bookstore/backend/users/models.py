from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    username=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    card_info=models.CharField(max_length=200,null=True)

    def get_user(self):
        return self.username
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_address(self):
        return self.address
    def get_password(self):
        return self.password
    def get_card_info(self):
        return self.card_info
   
