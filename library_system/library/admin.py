from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.timezone import now
from .models import Author, Publisher, Genre, Book, BookAuthor, BookCopy, Review

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

class BookInline(admin.TabularInline):
    model = Book.authors.through
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date', 'book_count', 'is_active')
    list_filter = ('birth_date',)
    search_fields = ('last_name', 'first_name', 'email')
    ordering = ('last_name', 'first_name')
    date_hierarchy = 'birth_date'
    inlines = [BookInline]

    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = "Number of Books"

    def is_active(self, obj):
        return obj.death_date is None
    is_active.boolean = True

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'established', 'book_count')
    list_filter = ('country', 'established')
    search_fields = ('name', 'city', 'country')

    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = "Number of Books"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'publication_date', 'is_available', 'rating', 'age')
    list_filter = ('genre', 'is_available', 'publication_date')
    search_fields = ('title', 'subtitle', 'isbn')
    ordering = ('-publication_date',)
    date_hierarchy = 'publication_date'
    list_editable = ('is_available', 'rating')
    list_per_page = 25
    save_on_top = True
    readonly_fields = ('created_at', 'updated_at', 'age')
    autocomplete_fields = ['publisher', 'genre']
    actions = ['mark_as_available', 'mark_as_unavailable']

    def age(self, obj):
        if not obj or not obj.publication_date:
            return "N/A"
        years = (now().date() - obj.publication_date).days // 365
        return f"{years} years"

    def mark_as_available(self, request, queryset):
        queryset.update(is_available=True)
    mark_as_available.short_description = "Mark selected books as available"

    def mark_as_unavailable(self, request, queryset):
        queryset.update(is_available=False)
    mark_as_unavailable.short_description = "Mark selected books as unavailable"

@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'copy_number', 'condition', 'is_borrowed', 'borrowed_by', 'due_date')
    list_filter = ('condition', 'is_borrowed')
    search_fields = ('book__title', 'borrowed_by__username')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('book__title', 'user__username', 'comment')