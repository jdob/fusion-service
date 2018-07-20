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

    def create(self, validated_data):
        created = self._save_partner(Partner(), validated_data)
        return created

    def update(self, instance, validated_data):
        updated = self._save_partner(instance, validated_data)
        return updated

    def _save_partner(self, partner, validated_data):
        partner.name = validated_data.get('name', '')
        partner.summary = validated_data.get('summary', '')
        partner.save()

        # Categories
        # TODO: This needs to change to look up the category instance and save that
        if 'categories' in validated_data:
            for c in validated_data['categories']:
                category = Category(partner=partner)
                category.name = c.get('name', '')
                category.save()

        # Contacts
        if 'contacts' in validated_data:
            for c in validated_data['contacts']:
                contact = Contact(partner=partner)
                contact.name = c.get('name', '')
                contact.email = c.get('email', '')
                contact.role = c.get('role', '')
                contact.save()

        # Engagements
        if 'engagements' in validated_data:
            for e in validated_data['engagements']:
                engagement = Engagement(partner=partner)
                engagement.notes = e.get('notes', '')
                engagement.location = e.get('location', '')
                engagement.attendees = e.get('attendees', '')
                engagement.save()

        # Comments
        if 'comments' in validated_data:
            for e in validated_data['comments']:
                comment = Comment(partner=partner)
                comment.text = e.get('text', '')
                comment.save()

        loaded = Partner.objects.get(pk=partner.id)
        return loaded

