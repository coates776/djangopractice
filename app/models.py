from django.db import models


class Place(models.Model):
    name = models.CharField('Place Name', max_length=120)
    address = models.CharField(max_length=300)
    postcode = models.CharField('Post Code', max_length=4)
    phone = models.CharField('Contact Phone', max_length=10)
    web = models.URLField('Web Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name


class AppUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Todolist(models.Model):
    item = models.CharField('Item Name', max_length=120)
    item_date = models.DateTimeField('Item Date')
    place = models.ForeignKey(Place, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=120)
    attendees = models.ManyToManyField(AppUser, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.item
