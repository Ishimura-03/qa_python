import pytest
from main import BooksCollector

class TestBooksCollector:
    
    # Тестируем добавление новой книги
    def test_add_new_book(self):
        collector  = BooksCollector()
        collector.add_new_book('Бойцовский клуб')
        assert collector.books_genre['Бойцовский клуб'] == ''

   # Тестируем установку жанра
    def test_set_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война миров')
        collector.set_book_genre('Война миров', 'Фантастика')
        assert collector.get_book_genre('Война миров') == 'Фантастика'

    # Тестируем получение жанра книги по его имени
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        assert collector.get_book_genre('Ведьмак') == 'Фантастика'

   # Тестируем вывод списка книг с определённым жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Град обречённый')
        collector.set_book_genre('Град обречённый', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Град обречённый']

    # Тестируем вывод книг, подходящих детям
    def test_get_books_for_children_is_true(self):
        collector = BooksCollector()
        collector.add_new_book('Чипполино')
        collector.set_book_genre('Чипполино', 'Комедии')
        assert 'Чипполино' in collector.get_books_for_children()
 
    # Тестируем, что книги, не подходящие детям, не выводятся
    def test_get_books_for_children_is_false(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Оно' not in collector.get_books_for_children()

   # Тестируем вдобавление книг без жанра
    def test_add_books_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гранатовый браслет')
        assert collector.get_books_with_specific_genre('') == [] 

   # Тестируем добавление книг в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Обитаемый остров')
        collector.add_book_in_favorites('Обитаемый остров')
        assert 'Обитаемый остров' in collector.get_list_of_favorites_books()

    # Тестируем удаление книг из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Обитаемый остров')
        collector.add_book_in_favorites('Обитаемый остров')
        collector.delete_book_from_favorites('Обитаемый остров')
        assert 'Обитаемый остров' not in collector.get_list_of_favorites_books()

    # Тестируем получение списка Избранных книг
    @pytest.mark.parametrize('book', [('12 стульев'), ('Про Федота-стрельца'), ('Золотой телёнок')])
    def test_get_list_of_favorites_books(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()

   
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Вино из одуванчиков')
        collector.set_book_genre('Вино из одуванчиков','Фантастика')
        assert collector.get_books_genre() == {'Вино из одуванчиков': 'Фантастика'}