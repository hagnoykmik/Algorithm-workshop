from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm, CommentForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()      # 인스턴스 생성
    context = {
        'article': article,
        'comment_form': comment_form,  # detail 템플릿에서 출력하기위함
    }
    return render(request, 'articles/detail.html', context)



@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

# pk
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)             # article의 pk(몇번째 글)를 사용하기 위해 조회
    comment_form = CommentForm(request.POST)         # data는 request.POST에 들어있다    
    if comment_form.is_valid():                      # 유효성 검사
        comment = comment_form.save(commit=False)    # 저장하면서 나올 객체를 미리 준다(저장X)
		comment.article = article                    # 몇 번째 게시글에 작성됐는지 
		comment.save()                               # 저장
		return redirect('articles:detail', article.pk)# 댓글이 써지고나면 댓글이 있는 페이지로