from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CategorySerializer, BookListSerializer, BookDetailSerializer
from .models import Category, Book
from .pagination import BookLimitOffsetPagination
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import render
from .filters import UserFilter
from django.core.mail import send_mail
from django.conf import settings

  



class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = BookLimitOffsetPagination


class FreeBookList(ListAPIView):
    queryset = Book.objects.filter(free=True)
    serializer_class = BookListSerializer
    pagination_class = BookLimitOffsetPagination


class BookList(ListAPIView):
    serializer_class = BookListSerializer
    pagination_class = BookLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Book.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query) |
                Q(category__category__icontains=query)


            ).distinct()
        return queryset_list


class BookDetailList(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class HomePage(ListView):
    context_object_name = 'home_list'    
    template_name = 'book/index.html'
    queryset = Book.objects.all()
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        allbook = Book.objects.all()
        paginator = Paginator(allbook, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
        context['book'] = file_exams
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'

    def get_context_data(self, **kwargs):
           context = super().get_context_data(**kwargs)
           context['now'] = timezone.now()
           return context

class BookListView(ListView):
    template_name = 'book/book.html'
    queryset = Book.objects.all()
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        allbook = Book.objects.all()
        paginator = Paginator(allbook, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
        context['book'] = file_exams
        return context


def BookFilter(request):
    book_list = Book.objects.all()
    book_filter = UserFilter(request.GET, queryset=book_list)
    return render(request, 'book/bookfilter.html', {'filter': book_filter})




def ContactForm(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        send_mail('Contact Form',
            message,
            settings.EMAIL_HOST_USER,
            ['baxtiyorovdilshod305@mail.ru'],
            fail_silently=False

            )
    return render(request, 'book/contact.html')


     