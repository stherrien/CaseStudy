from django.http import JsonResponse
from django.template.response import TemplateResponse
from .numbers_to_words import ConvertNumbersToWords
from rest_framework.decorators import api_view
from django.core.cache import cache
from rest_framework.response import Response


@api_view(['GET'])
def convert(request):
    converter = ConvertNumbersToWords()
    try:
        number = request.data["number"]
        cache_key = "CONVERT_NUMBER_%s" % number
        resp = ''
        if cache.get(cache_key, 'has expired') == 'has expired':
            was_converted, result = converter.convert(number)
            status = "ok" if was_converted else "failed"
            resp = {"status": status, "num_in_english": result}
            cache.set(cache_key, resp)
        else:
            resp = cache.get(cache_key)
        return Response(resp)
    except NameError as e:
        return Response({"status": "failed", "num_in_english": "name 'number' is not defined"})


def api_convert(request, number):
    converter = ConvertNumbersToWords()
    try:
        cache_key = "CONVERT_NUMBER_%s" % number
        resp = ''
        if cache.get(cache_key, 'has expired') == 'has expired':
            was_converted, result = converter.convert(number)
            status = "ok" if was_converted else "failed"
            resp = {"status": status, "num_in_english": result}
            cache.set(cache_key, resp)
        else:
            resp = cache.get(cache_key)
        return JsonResponse(resp)
    except NameError as e:
        return JsonResponse({"status": "failed", "num_in_english": "name 'number' is not defined"})


def index(request):
    t = TemplateResponse(request, 'index.html', {})
    return t.render()

