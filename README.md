# qa_python
## Что нужно сделать
Тестирование приложения ***BooksCollector***. Оно позволяет установить жанр книг и добавить их в избранное.

Класс ***BooksCollector*** содержит:
* Словарь ***books_genre***, куда можно добавить пару Название книги: Жанр книги.
* Список ***favorites***, который содержит избранные книги.
* Список ***genre***, который содержит доступные жанры.
* Список ***genre_age_rating***, который содержит жанры с возрастным рейтингом.

Набор методов для работы со словарем ***books_genre*** и списком ***favorites***:
* ***add_new_book*** — добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз.
* ***set_book_genre*** — устанавливает жанр книги, если книга есть в books_genreи её жанр входит в списокgenre.
* ***get_book_genre*** — выводит жанр книги по её имени.
* ***get_books_with_specific_genre*** — выводит список книг с определённым жанром.
* ***get_books_genre*** — выводит текущий словарь books_genre.
* ***get_books_for_children*** — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга.
* ***add_book_in_favorites*** — добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя.
* ***delete_book_from_favorites*** — удаляет книгу из избранного, если она там есть.
* ***get_list_of_favorites_books*** — получает список избранных книг.

```python
class BooksCollector:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']
    
    # добавляем новую книгу
    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    # устанавливаем книге жанр 
    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    # получаем жанр книги по её имени
    def get_book_genre(self, name):
        return self.books_genre.get(name)

    # выводим список книг с определённым жанром
    def get_books_with_specific_genre(self, genre):
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    # получаем словарь books_genre
    def get_books_genre(self):
        return self.books_genre

    # возвращаем книги, подходящие детям
    def get_books_for_children(self):
        books_for_children = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books_for_children.append(name)
        return books_for_children

    # добавляем книгу в Избранное
    def add_book_in_favorites(self, name):
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    # удаляем книгу из Избранного
    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    # получаем список Избранных книг
    def get_list_of_favorites_books(self):
        return self.favorites 
