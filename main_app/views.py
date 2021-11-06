from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Widget
from .forms import WidgetForm


def index(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})


class WidgetCreate(CreateView):
    model = Widget
    fields = "__all__"


def delete_widget(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('/')
