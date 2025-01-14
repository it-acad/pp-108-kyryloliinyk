from django.db import models, DataError

from authentication.models import CustomUser
from book.models import Book


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(default=None, null=True, blank=True)
    plated_end_at = models.DateTimeField(default=None)

    def __str__(self):
        return f'{self.book} ordered by {self.user}'

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'

    @staticmethod
    def create(user, book, plated_end_at):
        orders = Order.objects.all()
        books = set()
        for order in orders:
            if not order.end_at:
                books.add(order.book.id)
        if book.id in books and book.count == 1:
            return None
        try:
            order = Order(user=user, book=book, plated_end_at=plated_end_at)
            order.save()
            return order
        except ValueError:
            return None
        except DataError:
            return None

    @staticmethod
    def get_by_id(order_id):
        try:
            return Order.objects.get(pk=order_id)
        except:
            return None

    def update(self, plated_end_at=None, end_at=None):
        if plated_end_at != None:
            self.plated_end_at = plated_end_at
        if end_at != None:
            self.end_at = end_at
        self.save()

    @staticmethod
    def get_all():
        return list(Order.objects.all())

    @staticmethod
    def get_not_returned_books():
        return Order.objects.filter(end_at=None).values()

    @staticmethod
    def delete_by_id(order_id):
        try:
            a = Order.objects.get(pk=order_id)
        except:
            return False
        else:
            a.delete()
            return True
