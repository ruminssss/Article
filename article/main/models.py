from django.db import models

class Art(models.Model):
    title = models.CharField(max_length=50, verbose_name='Загаловок')
    content = models.TextField(verbose_name='Содержимое')
    author = models.CharField(max_length=50, verbose_name='Пользователь', default='пользователь')
    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'

class Comment(models.Model):
    content = models.TextField(verbose_name='комментарий')
    author = models.CharField(max_length=50, verbose_name='автор')
    art = models.ForeignKey(Art, on_delete=models.CASCADE, verbose_name='Пожайлуста, не трогайте этот параметр(недоделка осталась на моей совести)')
    list_display = ('content', 'author', 'art')
    class Meta:
        verbose_name_plural = 'комментарии'
        verbose_name = 'комментарий'