from django.db import models

class Testimonial(models.Model):
    testimonial_id = models.AutoField
    said_by = models.CharField(max_length=255,default='')
    post = models.CharField(max_length=255,default='')
    testimonial_string = models.CharField(max_length=10000, default="")
    image = models.ImageField(upload_to="images", default='')
    def __str__(self):
        return self.post+ ' ' + self.said_by

class Advisor(models.Model):
    advisor_id = models.AutoField
    advisor_name = models.CharField(max_length=255,default='')
    advisor_post = models.CharField(max_length=255,default='')
    advisor_image = models.ImageField(upload_to="images", default='')
    def __str__(self):
        return self.advisor_post

class leader(models.Model):
    leader_id = models.AutoField
    name = models.CharField(max_length=255,default='')
    post = models.CharField(max_length=255,default='')
    image = models.ImageField(upload_to="images", default='')
    year = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.post + ' ' + self.name

class BOD(models.Model):
    bod_id = models.AutoField
    name = models.CharField(max_length=255,default='')
    post = models.CharField(max_length=255,default='')
    image = models.ImageField(upload_to="images", default='')
    facebook_link = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.post + ' ' + self.name
class Committee(models.Model):
    committee_id = models.AutoField
    name = models.CharField(max_length=255,default='')
    post = models.CharField(max_length=255,default='')
    image = models.ImageField(upload_to="images", default='')
    facebook_link = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.post + ' ' + self.name

class Service(models.Model):
    service_id = models.AutoField
    title = models.CharField(max_length=255,default='')
    string = models.CharField(max_length=10000,default='')
    image = models.ImageField(upload_to="images", default='')
    def __str__(self):
        return self.title