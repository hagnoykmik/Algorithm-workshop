from pyexpat import model
from django.db import models

# 스키마 구성 - Class형태로 구성
class Article(models.Model):
    # column = models.타입(ModelFeild)(제약조건(option))
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 댓글을 구성하는 테이블을 만들자!
# 댓글 테이블 스키마
# models모듈의 Model 클래스를 상속받을 거임
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()        # 글자 수 제한 X
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

# 다했으면 migration 해줘야한다
