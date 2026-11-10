from django.contrib import admin
from .models import Books,BooksReviews,bookstore,ISBN


class BookReviewInline(admin.TabularInline):
    model = BooksReviews
    extra = 2


class Bookslist(admin.ModelAdmin):
    fields = ('category', 'name', 'author', 'price', 'description', 'img',)
    list_display = ('category', 'name', 'author', 'price', 'img',)
    search_fields = ('name',)
    list_filter = ('category',)
    inlines = [BookReviewInline]
   

class storeadmin(admin.ModelAdmin):
    list_display = ('name','location','available_books')
    filter_horizontal = ('books',)
    
    def available_books(self, obj):
        return " , ".join(str(book) for book in obj.books.all())
    
    
    #def __str__(self):
    #    return self.name
class isbnadmin(admin.ModelAdmin):
    fields= ('name','pages','isbn_number')
    list_display = ('name','isbn_number','pages',)  

admin.site.register(Books, Bookslist)
admin.site.register(bookstore, storeadmin)
admin.site.register(ISBN, isbnadmin)

