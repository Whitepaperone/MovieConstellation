from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import JsonResponse


# 이쪽이 VUE랑 연동해서 쓸 모듈들
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    )
from .models import Review
from .serializers import PlayListListSerializer, PlayListSerializer


@api_view(['GET', 'POST'])
def playlist_list(request):
    if request.method == 'GET':
        playlists = get_list_or_404(Review)
        serializer =PlayListListSerializer(playlists, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PlayListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    


# @require_http_methods(['GET', 'POST'])
# def create(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST) 
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user
#             review.save()
#             return redirect('community:detail', review.pk)
#     else:
#         form = ReviewForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'community/create.html', context)


# @require_GET
# def detail(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     comments = review.comment_set.all()
#     comment_form = CommentForm()
#     context = {
#         'review': review,
#         'comment_form': comment_form,
#         'comments': comments,
#     }
#     return render(request, 'community/detail.html', context)

# @require_POST
# def create_comment(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.review = review
#         comment.user = request.user
#         comment.save()
#         return redirect('community:detail', review.pk)
#     context = {
#         'comment_form': comment_form,
#         'review': review,
#         'comments': review.comment_set.all(),
#     }
#     return render(request, 'community/detail.html', context)


# @require_POST
# def like(request, review_pk):
#     if request.user.is_authenticated:
#         review = get_object_or_404(Review, pk=review_pk)
#         user = request.user

#         if review.like_users.filter(pk=user.pk).exists():
#             review.like_users.remove(user)
#             is_liked = False
#         else:
#             review.like_users.add(user)
#             is_liked = True
        
#         like_count = review.like_users.count()    
#         context = {
#             'like_count': like_count,
#             'is_liked': is_liked,
#         }
#         return JsonResponse(context)
#     return redirect('accounts:login')
