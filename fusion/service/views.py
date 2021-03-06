from rest_framework import (decorators, parsers, renderers, response, viewsets)
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView

from .models import (Category, Comment, Contact, Engagement, Link, Partner, Task)
from .serializers import (CategorySerializer, CommentSerializer, ContactSerializer,
                          EngagementSerializer, LinkSerializer, PartnerSerializer,
                          TaskSerializer)


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
            return self._delete_engagement(engagement_id)
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

    @staticmethod
    def _delete_engagement(engagement_id):
        Engagement.objects.filter(id=engagement_id).delete()
        return response.Response({})

    @staticmethod
    def _update_engagement(request, engagement_id):
        e = Engagement.objects.get(pk=engagement_id)
        for key,value in request.data['changes'].items():
            setattr(e, key, value)
        e.save()
        return response.Response(EngagementSerializer(e).data)

    @decorators.detail_route(methods=['get', 'post', 'delete', 'patch'], url_path='comments')
    def comments(self, request, pk=None, comment_id=None):

        if self.request.method == 'GET':
            return self._get_comments()
        elif self.request.method == 'POST':
            return self._create_comment(request)
        elif self.request.method == 'DELETE':
            return self._delete_comment(comment_id)
        elif self.request.method == 'PATCH':
            return self._update_comment(request, comment_id)

    def _get_comments(self):
        comments = Comment.objects.filter(partner=self.get_object())
        s = CommentSerializer(comments, many=True)
        return response.Response(s.data)

    def _create_comment(self, request):
        s = CommentSerializer()
        request.data['partner'] = self.get_object()
        e = s.create(request.data)
        return response.Response(s.to_representation(e))

    @staticmethod
    def _delete_comment(comment_id):
        Comment.objects.filter(id=comment_id).delete()
        return response.Response({})

    @staticmethod
    def _update_comment(request, comment_id):
        Comment.objects.filter(id=comment_id).update(text=request.data['text'])
        return response.Response({})

    @decorators.detail_route(methods=['get', 'post', 'delete', 'patch'], url_path='contacts')
    def contacts(self, request, pk=None, contact_id=None):

        if self.request.method == 'GET':
            return self._get_contacts()
        elif self.request.method == 'POST':
            return self._create_contact(request)
        elif self.request.method == 'DELETE':
            return self._delete_contact(contact_id)
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

    @staticmethod
    def _delete_contact(contact_id):
        Contact.objects.filter(id=contact_id).delete()
        return response.Response({})

    @staticmethod
    def _update_contact(request, contact_id):
        c = Contact.objects.get(pk=contact_id)
        for key,value in request.data['changes'].items():
            setattr(c, key, value)
        c.save()
        return response.Response({})

    @decorators.detail_route(methods=['get', 'post', 'delete', 'patch'], url_path='links')
    def links(self, request, pk=None, link_id=None):
        if self.request.method == 'GET':
            return self._get_links()
        elif self.request.method == 'POST':
            return self._create_link(request)
        elif self.request.method == 'DELETE':
            return self._delete_link(link_id)
        elif self.request.method == 'PATCH':
            return self._update_link(request, link_id)

    def _get_links(self):
        links = Link.objects.filter(partner=self.get_object())
        ls = LinkSerializer(links, many=True)
        return response.Response(ls.data)

    def _create_link(self, request):
        ls = LinkSerializer()
        request.data['partner'] = self.get_object()
        e = ls.create(request.data)
        return response.Response(ls.to_representation(e))

    @staticmethod
    def _delete_link(link_id):
        Link.objects.filter(id=link_id).delete()
        return response.Response({})

    @staticmethod
    def _update_link(request, link_id):
        link = Link.objects.get(pk=link_id)
        for key, value in request.data['changes'].items():
            setattr(link, key, value)
        link.save()
        serializer = LinkSerializer()
        return response.Response(serializer.to_representation(link))

    @decorators.detail_route(methods=['get', 'post', 'delete', 'patch'], url_path='tasks')
    def tasks(self, request, pk=None, task_id=None):

        if self.request.method == 'GET':
            return self._get_tasks()
        elif self.request.method == 'POST':
            return self._create_task(request)
        elif self.request.method == 'DELETE':
            return self._delete_task(task_id)
        elif self.request.method == 'PATCH':
            return self._update_task(request, task_id)

    def _get_tasks(self):
        tasks = Task.objects.filter(partner=self.get_object())
        t = TaskSerializer(tasks, many=True)
        return response.Response(t.data)

    def _create_task(self, request):
        t = TaskSerializer()
        request.data['partner'] = self.get_object()
        e = t.create(request.data)
        return response.Response(t.to_representation(e))

    @staticmethod
    def _delete_task(task_id):
        Task.objects.filter(id=task_id).delete()
        return response.Response({})

    @staticmethod
    def _update_task(request, task_id):
        task = Task.objects.get(pk=task_id)
        for key, value in request.data['changes'].items():
            setattr(task, key, value)
        task.save()
        serializer = TaskSerializer()
        return response.Response(serializer.to_representation(task))


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FusionAuthView(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Load the token
        token, created = Token.objects.get_or_create(user=user)

        # Look up the user's groups
        group_names = [g.name for g in user.groups.all()]

        # Package up for the caller
        response_data = {
            'token': token.key,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'groups': group_names,
            'is_superuser': user.is_superuser,
        }

        return response.Response(response_data)
