from django.db import models
import datetime 

class Partner(models.Model):

    name = models.CharField(max_length=256, unique=True)
    summary = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    logo = models.TextField(null=True)  # base64

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class PartnerCategory(models.Model):

    partner = models.ForeignKey(Partner, related_name='categories', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'partner_categories'

    def category_id(self):
        return self.category.id

    def category_name(self):
        return self.category.name


class Engagement(models.Model):

    partner = models.ForeignKey(Partner, related_name='engagements', on_delete=models.CASCADE)

    notes = models.TextField()
    location = models.CharField(max_length=256, null=True)
    timestamp = models.DateTimeField(default=datetime.date.today)
    attendees = models.TextField(null=True)  # comma-separated


class Contact(models.Model):

    partner = models.ForeignKey(Partner, related_name='contacts', on_delete=models.CASCADE)

    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=256, null=True)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):

    partner = models.ForeignKey(Partner, related_name='comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=256, null=True)
    
    def __str__(self):
        return self.text


class Link(models.Model):

    partner = models.ForeignKey(Partner, related_name='links', on_delete=models.CASCADE)
    url = models.TextField()
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)

    class Meta:
        unique_together = ('partner', 'url')

    def __str__(self):
        return self.name

# completed can have only 3 values 
# 0 - not completed
# 1 - completed
# 2 - archived
class Task(models.Model):

    partner = models.ForeignKey(Partner, related_name='tasks', on_delete=models.CASCADE)
    text = models.CharField(max_length=256, null=True)
    completed = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text
