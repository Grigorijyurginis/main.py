from django.db import models

class Forms (models.Model):
    name = models.CharField('Имя', max_length=30)
    sourname = models.CharField('Фамилия', max_length=30)
    age = models.DateField('Дата рождения')
    comment = models.TextField('О себе')

    def __str__(self):
        return self.name
