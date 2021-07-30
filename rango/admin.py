from django.contrib import admin
from rango.models import Category, Page, UserProfile

class PageInLine(admin.TabularInline):
    model = Page
    extra = 4

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    fieldsets = [
        (None,                  {'fields' : ['name', 'slug']}),
        ('Engagement Info',     {'fields' : ['likes', 'views'], 'classes' : ['collapse']}),
    ]
    inlines = [PageInLine]
    list_display = ('name', 'likes', 'views', 'slug')


admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    fields = [ 'title', 'category', 'url']
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)

# Register your models here.
