from .models import  Book
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = [ 'category', 'name',  'free']

 


      