import asyncio

from rest_framework.exceptions import ValidationError
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from wildberries.services import (
    get_articles_from_file,
    get_data_from_wildberries,
)


class WildberriesView(APIView):
    parser_classes = (JSONParser, FileUploadParser)

    def post(self, request, *args, **kwargs):
        articles = self._get_articles(request)
        data = asyncio.run(get_data_from_wildberries(articles))
        return Response(data=data, content_type="application/json")

    def _get_articles(self, request) -> list:
        return self._validation(request)

    @staticmethod
    def _validation(request) -> list:
        file_obj = request.data.get('file')
        article = request.data.get('article')
        if file_obj and article:
            raise ValidationError("Only a file or an article must be sent")
        elif file_obj is None and article is None:
            raise ValidationError("At least a file or an article must be sent")
        elif article:
            articles = [article]
        else:
            try:
                articles = get_articles_from_file(file_obj)
            except ValueError:
                raise ValidationError("Bad file")
        return articles
