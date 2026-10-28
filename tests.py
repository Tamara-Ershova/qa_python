import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize(
            'name',
            ['Я','Я' * 20,'Я' * 40]
    )

    def test_add_new_book_add_valid_name_length(self, collector, name):
        collector.add_new_book(name)
    
        assert len(collector.get_books_genre()) == 1


    def test_add_new_book_add_same_book_not_added(self, collector):
        collector.add_new_book('Тарзан')
        collector.add_new_book('Тарзан')

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_genre_success(self, collector):   
        collector.add_new_book('Каникулы в Простоквашино')
        collector.set_book_genre('Каникулы в Простоквашино','Мультфильмы')

        assert collector.books_genre['Каникулы в Простоквашино'] == 'Мультфильмы'

    def test_get_book_genre_positive(self, collector):
        collector.add_new_book('Каникулы в Простоквашино')
        collector.set_book_genre('Каникулы в Простоквашино','Мультфильмы')
        
        assert collector.get_book_genre('Каникулы в Простоквашино') == 'Мультфильмы'

    def test_get_books_with_specific_genre_in_genre_list(self, collector):
        collector.add_new_book('Каникулы в Простоквашино')
        collector.set_book_genre('Каникулы в Простоквашино','Мультфильмы')

        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Каникулы в Простоквашино']

    def test_get_books_genre_one_book_in_dictionary(self, collector):
        collector.add_new_book('Каникулы в Простоквашино')
        collector.set_book_genre('Каникулы в Простоквашино','Мультфильмы')

        assert collector.get_books_genre() == {'Каникулы в Простоквашино':'Мультфильмы'}

    @pytest.mark.parametrize(
            'name,genre',
            [
                ('Сияние', 'Ужасы'),
                ('Пуаро', 'Детективы')
            ]
    )

    def test_get_books_for_children_age_rating_books_not_in_list(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
                
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_same_book_not_added (self, collector):
        collector.add_new_book('Отцы и Дети')
        collector.add_book_in_favorites('Отцы и Дети')
        collector.add_book_in_favorites('Отцы и Дети')
        
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_deleted_book_not_in_favorites(self, collector):
        collector.add_new_book('Отцы и Дети')
        collector.add_book_in_favorites('Отцы и Дети')
        collector.delete_book_from_favorites('Отцы и Дети')

        assert 'Отцы и Дети' not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Отцы и Дети')
        collector.add_book_in_favorites('Отцы и Дети')

        assert collector.get_list_of_favorites_books() == ['Отцы и Дети']



