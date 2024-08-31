from django.db import models


class Quizz(models.Model):
    grade = models.TextField('класс', max_length=500)
    title = models.TextField('Название, класс, предмет', max_length=500)
    url = models.TextField('Ссылка', max_length=5000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/quiz/{self.id}'

    class Meta:
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квиз'
