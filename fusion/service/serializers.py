from rest_framework import serializers

from fusion.service.models import (Category, Comment, Contact, Engagement,
                                   Link, Partner, PartnerCategory)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'role', 'notes')


class EngagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Engagement
        fields = ('id', 'notes', 'location', 'timestamp', 'attendees')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'text')


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ('id', 'url', 'name', 'description')


class PartnerCategorySerializer(serializers.ModelSerializer):

    category_id = serializers.CharField()
    name = serializers.CharField(source='category_name')

    class Meta:
        model = PartnerCategory
        fields = ('category_id', 'name')


class PartnerSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, required=False)
    engagements = EngagementSerializer(many=True, required=False)
    comments = CommentSerializer(many=True, required=False)
    categories = PartnerCategorySerializer(many=True, required=False)
    links = LinkSerializer(many=True, required=False)

    class Meta:
        model = Partner
        fields = ('id', 'name', 'summary', 'logo', 'created', 'updated', 'links',
                  'contacts', 'engagements', 'comments', 'categories')
