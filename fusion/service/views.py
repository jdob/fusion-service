from rest_framework import (decorators, response, viewsets)

from .models import (Engagement, Partner, Comment, Category, Contact)
from .serializers import (EngagementSerializer, PartnerSerializer, CommentSerializer, CategorySerializer, ContactSerializer)


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

    @decorators.detail_route(methods=['get', 'post', 'delete', 'patch'], url_path='engagements')
    def engagements(self, request, pk=None, engagement_id=None):

        if self.request.method == 'GET':
            return self._get_engagements()
        elif self.request.method == 'POST':
            return self._create_engagement(request)
        elif self.request.method == 'DELETE':
            return self._delete_engagement(request, engagement_id)
        elif self.request.method == 'PATCH':
            return self._update_engagement(request, engagement_id)

    def _get_engagements(self):
        engagements = Engagement.objects.filter(partner=self.get_object())
        s = EngagementSerializer(engagements, many=True)
        return response.Response(s.data)

    def _create_engagement(self, request):
        s = EngagementSerializer()
        request.data['partner'] = self.get_object()
        e = s.create(request.data)

        return response.Response(s.to_representation(e))

    def _delete_engagement(self, request, engagement_id):
        Engagement.objects.filter(id=engagement_id).delete()
        return response.Response({})

    def _update_engagement(self, request, engagement_id):
        e = Engagement.objects.get(pk=engagement_id)
        for key,value in request.data['changes'].items():
            setattr(e, key, value)
            e.save()
        return response.Response(EngagementSerializer(e).data)

    @decorators.detail_route(methods=['get', 'post', 'delete', 'patch'], url_path='comments')
    def comments(self, request, pk=None, comment_id=None):

        if self.request.method == 'GET':
            return self._get_comments(request)
        elif self.request.method == 'POST':
            return self._create_comment(request)
        elif self.request.method == 'DELETE':
            return self._delete_comment(request, comment_id)
        elif self.request.method == 'PATCH':
            return self._update_comment(request, comment_id)

    def _get_comments(self, request):
        comments = Comment.objects.filter(partner=self.get_object())
        s = CommentSerializer(comments, many=True)
        return response.Response(s.data)

    def _create_comment(self, request):
        s = CommentSerializer()
        request.data['partner'] = self.get_object()
        e = s.create(request.data)
        return response.Response(s.to_representation(e))

    def _delete_comment(self, request, comment_id):
        Comment.objects.filter(id=comment_id).delete()
        return response.Response({})

    def _update_comment(self, request, comment_id):
        Comment.objects.filter(id=comment_id).update(text=request.data['text'])
        return response.Response({})

    #CRUD for contacts    
    @decorators.detail_route(methods=['get', 'post', 'delete', 'patch'], url_path='contacts')
    def contacts(self, request, pk=None, contact_id=None):

        if self.request.method == 'GET':
            return self._get_contacts()
        elif self.request.method == 'POST':
            return self._create_contact(request)
        elif self.request.method == 'DELETE':
            return self._delete_contact(request, contact_id)
        elif self.request.method == 'PATCH':
            return self._update_contact(request, contact_id)

    def _get_contacts(self):
        contacts = Contact.objects.filter(partner=self.get_object())
        c = ContactSerializer(contacts, many=True)
        return response.Response(c.data)

    def _create_contact(self, request):
        c = ContactSerializer()
        request.data['partner'] = self.get_object()
        e = c.create(request.data)

        return response.Response(c.to_representation(e))

    def _delete_contact(self, request, contact_id):
        Contact.objects.filter(id=contact_id).delete()
        return response.Response({})

    def _update_contact(self, request, contact_id):
        c = Contact.objects.get(pk=contact_id)
        for key,value in request.data['changes'].items():
            setattr(c, key, value)
            c.save()
        return response.Response({})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

