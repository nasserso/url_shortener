from rest_framework import viewsets
from shortener.models import Shortener
from shortener.serializers import ShortnerCreateSerializer, ShortnerSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class ShortnerViewSet(viewsets.ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = ShortnerSerializer
    # TODO: por usuario?
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return ShortnerCreateSerializer
        return ShortnerSerializer

    @action(detail=False, url_path=r"(?P<slang>\w+)")
    def unshort(self, request, slang=None):
        try:
            url_qs = self.queryset.get(slang=slang)
        except:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(url_qs)
        return Response(serializer.data)
