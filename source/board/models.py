from django.db import models


class Board(models.Model):
    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = verbose_name

    title = models.CharField('제목', max_length=100, blank=True)
    content = models.TextField('내용', blank=True)

    def __str__(self):
        return f'<{self.id}> {self.title}'

