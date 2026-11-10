from django.shortcuts import render,get_object_or_404
from .models import Books,ISBN,bookstore
from .forms import Books_form
# Create your views here.
def home(request):
    books = Books.objects.all()
    
    
    return render(request,'books.html',{'books':books})


def bookdetails(request, pk):
    book = get_object_or_404(Books,pk=pk)
    isbn = ISBN.objects.all()
    return render(request,'book_detailed.html',{'book':book,'isbn':isbn,})


def book_store(request):
    store = None

    if request.method == 'POST':
        form = Books_form(request.POST)
        if form.is_valid():
            book_value = form.cleaned_data['Books']
            store = bookstore.objects.filter(books=book_value)
    else:
        form = Books_form()

    return render(request, 'store.html', {
        'form': form,
        'store': store
    })