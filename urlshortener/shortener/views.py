from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShortURLSerializer
from django.http import HttpResponse
from .models import ShortURL


@api_view(["POST"])
def shorten_url(request):
    serializer = ShortURLSerializer(data=request.data)
    if serializer.is_valid():
        short_url = serializer.save()
        return Response({ "original_url": short_url.original_url, "short_code": short_url.short_code, "short_url": f"http://localhost:8000/{short_url.short_code}" }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """if request.method == "POST":
        original_url = request.POST.get('original_url')
        short_url = ShortURL.objects.create(original_url=original_url)
        return HttpResponse(f"Short URL: http://localhost:8000/{short_url.short_code}")
    return render(request, 'index.html')"""


@api_view(['GET'])
def redirect_url(request, short_code):
    url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(url.original_url)