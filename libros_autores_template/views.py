from libros_autores_template.models import Authors, Books
from django.shortcuts import render, redirect, HttpResponse


#path('landing/', views.index), renderiza landing.html CHECK
    #path('books/', views.books), direcciona a /books y renderea books.html CHECK
    #path('authors/', views.author), direcciona a /authors y renderea authors.html
    
def index(request):
    libros = Books.objects.all()
    autores = Authors.objects.all()
    context = {
        'books' : libros,
        'authors': autores,
    }
    return render(request, 'landing.html', context)#check


def books(request):
    libros = Books.objects.all()
    context = {
        'books' : libros,
    }
    return render(request, 'books.html', context)#check


def authors(request):
    autores = Authors.objects.all()
    context = {
        'authors': autores,
    }
    return render(request, 'Authors.html', context) #CHECK


def addbook(request):
    titulo = request.POST['title_input']
    descripcion = request.POST['desc_input']
    new_book = Books.objects.create(title = titulo, desc = descripcion)
    return redirect('/books') #CHECK

def addauthor(request):
    first_name = request.POST['first_name_input'] 
    last_name = request.POST['last_name_input']
    desc = request.POST['last_name_input']
    new_author= Authors.objects.create(first_name= first_name, last_name= last_name, desc = desc)
    return redirect('/authors') #CHECK


def deploybook(request, nom):
    
    this_book= Books.objects.get(id = nom)
    this_book_authors = this_book.authors.all()
    free_authors = [author for author in Authors.objects.all() if author.id not in this_book_authors]
    libros = Books.objects.all()
    autores = Authors.objects.all()

    if request.method == 'GET':
        context = {
            'books' : libros,
            'authors': autores,
            'this_book': this_book,
            'this_book_authors': this_book_authors,
            'free_authors': free_authors,
            
        }
        return render(request,"books_output.html", context)

    else:
        this_author_id = int(request.POST['author_id'])
        this_author = Authors.objects.get(id= this_author_id)
        new_books_author = this_book.authors.add(this_author)
        new_books_author.save()
        this_author.save()
        
        #messages.success('The author has successfully linked to the book')
    return redirect(f'/books/{nom}')

def deployauthor(request, nam):
    this_num = int(nam)
    this_author= Authors.objects.get(id = this_num)
    libros = Books.objects.all()
    autores = Authors.objects.all()
    this_authors_books = this_author.books.all()
    free_books = [book for book in Books.objects.all() if book.id not in this_authors_books]

    if request.method == 'GET':
        context = {
            'books' : libros,
            'authors': autores,
            'this_author': this_author,
            'this_authors_books': this_authors_books,
            'free_books': free_books,
        }
        return render(request, 'authors_output.html', context)

    else:
        this_book_id= int(request.POST['book_id'])
        this_book = Books.objects.get(id= this_book_id)
        new_author_books = this_author.books.add(this_book)
        new_author_books.save()

    return redirect(f'/authors/{nam}/')


'''
path('authors/', views.authors),
    path('addbook/', views.addbook),
    path('addauthor/', views.addauthor),
    path('books/<name>/', views.deploybook),
    path('authors/<name>/',views.deployauthor),
    path('deploybook/', views.addauthortobook),
    path('deployauthor/', views.addbooktoauthor),

    '''