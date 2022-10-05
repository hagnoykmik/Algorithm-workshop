from dataclasses import field
from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='제목',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'my-title',
    #             'placeholder': 'Enter the title',
    #             'maxlength': 10,
    #         }
    #     )
    # )

    # content = forms.CharField(
    #     label='내용',
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'my-content',
    #             'placeholder': 'Enter the content',
    #             'rows': 5,
    #             'cols': 50,
    #         }
    #     ),
    #     error_messages={
    #         'required': '내용을 입력하세요.',
    #     }
    # )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)

# forms 라이브러리에 있는 ModelForm 클래스 상속
class CommentForm(forms.ModelForm):
    # CommentForm에 대한 정보를 작성하는 곳
    class Meta:
        model = Comment
        # fields = '__all__'   # 전체 필드 출력
        exclude = ('article',)