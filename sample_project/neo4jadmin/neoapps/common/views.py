from django.shortcuts import render, redirect
from neoapps.common.models import Country, Language
from neoapps.user.models import User
from neoapps.author.models import Author
from neoapps.book.models import Book

from neomodel import install_labels

def index(request):

    # install_labels(Book)

    dr = Author.nodes.get(uid='13a6e8cce02446bd8434919fc16dea23')
    pbook = Book(uid='c841c1ba79a342c492a349752adc7dd0')

    # print(pbook)

    insertbook()
    # # dr.full_name="Dr Sina Saderi"
    # # dr.save()

    # iran = Country.nodes.get(country_code='ir')
    # langauges = Language.nodes.all()

    # fa = langauges[0]
    # en = langauges[1]

    # print(dr)
    # print(iran)
    # print("fa", fa)
    # print("en", en)

    # pbook.author.connect(dr)
    # # dr.country.connect(iran)
    # # dr.language.connect(fa)
    # # dr.language.connect(en)

    context = {
        'sss' :'sssss'
    }

    return render(request, 'common/index.html', context)

def insertbook():
    # book = Book(title="Artifical inteligence", slug="arti-inte", summary="smallllll", desc="deeeeeeeeeeeee", image="http://localhost:3000/assets/images/books/book_1.png")
    # book.save()
    # book = Book(uid='c841c1ba79a342c492a349752adc7dd0')
    # print(book)
    # book.delete()
    # dr = Author.nodes.get(uid='13a6e8cce02446bd8434919fc16dea23')
    # book.author.connect(dr)
    pass

    
