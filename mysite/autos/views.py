from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make
from autos.forms import MakeForm

# Create your views here.

#A lis view for autos (Retrive/Read/Select) ----------------------------

class MainView(LoginRequiredMixin, View):
# the above code means the user is required to
# login to view this page

    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'autos/auto_list.html', ctx)


# a list view for make (Retrive/Read/Select) ----------------------

# Take the easy way out on the make table
# These views do not need a form because CreateView,UpdateView and DeleteView
# Build a form object dynamically based on the fields
# value in the constructor attributes

class MakeView(LoginRequiredMixin, View):
# the above code means the user is required to
# login to view this page

    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)


# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded

# create -------> make model
class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView

# update -------> make model
class MakeUpdate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# delete -------> make model
class MakeDelete(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# Take the easy way out on the autos table
# These views do not need a form because CreateView,UpdateView and DeleteView
# Build a form object dynamically based on the fields
# value in the constructor attributes

# create -------> auto model
class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# update -------> auto
class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# delete -------> auto
class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview
