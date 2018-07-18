from django.db import models


class Partner(models.Model):

    name = models.CharField(max_length=256)
    summary = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    links = models.TextField(null=True)  # comma-separated
    logo = models.TextField(null=True)  # base64

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=256)
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
    timestamp = models.DateTimeField(auto_now=True)
    attendees = models.TextField(null=True)  # comma-separated


class Contact(models.Model):

    partner = models.ForeignKey(Partner, related_name='contacts', on_delete=models.CASCADE)

    name = models.CharField(max_length=256)
    email = models.EmailField()
    role = models.CharField(max_length=256, null=True)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):

    partner = models.ForeignKey(Partner, related_name='comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=256, null=True)
    
    def __str__(self):
        return self.text
