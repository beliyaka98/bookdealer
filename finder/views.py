from django.shortcuts import render
from .forms import SearchForm
from . import flip
from . import wilberries
from . import kaspi


def main(request):
    form = SearchForm()
    if request.GET.get('book_name'):
        flip_books = flip.search_book_flip(request.GET.get('book_name'))
        wild_books = wilberries.search_book_wildberries(request.GET.get('book_name'))
        kaspi_books = kaspi.search_book_kaspi(request.GET.get('book_name'))
        return render(request, 'finder/search_results.html', context={'form': form, 'flip_books': flip_books, 'wild_books': wild_books, 'kaspi_books': kaspi_books})
    return render(request, 'finder/main.html', context={'form': form})