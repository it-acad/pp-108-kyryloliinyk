from django.db import models

import book.models


class Author(models.Model):
    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=20)
    patronymic = models.CharField(blank=True, max_length=20)
    books = models.ManyToManyField(book.models.Book, related_name='authors')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __repr__(self):
        return f"Author(id={self.pk})"

    @staticmethod
    def delete_by_id(author_id):
        try:
            author = Author.objects.get(pk=author_id)
            author.delete()
            return True
        except:
            return False

    @staticmethod
    def create(name, surname, patronymic):
        if name and len(name) <= 20 and surname and len(surname) <= 20 and patronymic and len(patronymic) <= 20:
            author = Author(name=name, surname=surname, patronymic=patronymic)
            author.save()
            return author

    @staticmethod
    def get_all():
        return Author.objects.all()
