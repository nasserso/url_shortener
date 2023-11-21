from rest_framework import viewsets
from shortener.models import Shortener
from shortener.serializers import ShortnerCreateSerializer, ShortnerSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class ShortnerViewSet(viewsets.ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = ShortnerSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return ShortnerCreateSerializer
        return ShortnerSerializer

    @action(detail=False, url_path=r"(?P<slang>\w+)")
    def unshort(self, request, slang=None):
        try:
            url_data = self.queryset.get(slang=slang)
        except:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)

        url_data.access_counter += 1
        url_data.save()

        serializer = self.get_serializer(url_data)
        return Response(serializer.data)
