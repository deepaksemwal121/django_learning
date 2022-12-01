from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "A good title",
            subtitle = "Lorem Ipsuma dolar and friends are watching his boys and met him in a zoo and now don't",
            author ="Ashutosh",
            isbn="12123123"
        )
    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtitle, "Lorem Ipsuma dolar and friends are watching his boys and met him in a zoo and now don't")
        self.assertEqual(self.book.author, "Ashutosh")
        self.assertEqual(self.book.isbn, "12123123")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lorem Ipsum")
        self.assertTemplateUsed(response, "books/book_list.html")