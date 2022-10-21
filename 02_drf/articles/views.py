from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from articles.serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment


# 목록
@api_view(['GET', 'POST']) 
def article_list(request):
    # 조회
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data) 

    # 생성
    elif request.method == 'POST':
        # ArticleForm(request.POST)
        # 전체 필드를 모두 serialize해서 serializer에 받는다
        serializer = ArticleSerializer(data=request.data)
        # 저장 전에 유효성 검사
        if serializer.is_valid():
            serializer.save()
            # 성공 (201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 실패 (400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# 단일
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)  # 공통 코드
    article = get_object_or_404(Article, pk=article_pk) # 못찾았을 때 404 예외를 발생시킴
    
    # 게시글 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data) 

    # 게시글 삭제
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 게시글 수정
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

# 댓글
# 목록
@api_view(['GET']) 
def comment_list(request):
    # 조회
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data) 

# 단일 댓글 
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)  # 공통 코드
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    # 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data) 

    # 댓글 삭제
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 댓글 수정
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)








@api_view(['POST'])
def comment_create(request, article_pk):
		# article 객체 조회
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)