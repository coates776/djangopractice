from django.shortcuts import render

from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Todolist, AppUser
from django.http import HttpResponseRedirect
from .forms import PlaceForm
from django.core.paginator import Paginator


def index(request, year=date.today().year, month=date.today().month):
    month = int(month)
    year = int(year)
    if year < 2000 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "My Todo List - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)

    announcements = [
        {
            'date': '6-10-2022',
            'announcement': "Site registration opens"
        },

        {
            'date': '6-10-2020',
            'announcement': "Site registration opens"
        }
    ]
    # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    return render(request, 'app/calendar_base.html', {'title': title, 'cal': cal, 'announcements': announcements})


def all_todolist(request):
    all_todo_list = Todolist.objects.all()
    return render(request, 'app/todolist.html', {'all_todo_list': all_todo_list})


def add_place(request):
    submitted = False
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/add_place/?submitted=True')
    else:
        form = PlaceForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'app/add_place.html',
                  {'form': form, 'submitted': submitted})


def list_subscriber(request):
    p = Paginator(AppUser.objects.all(), 3)
    page = request.GET.get('page')
    subscribers = p.get_page(page)
    return render(request,
                  'app/subscribers.html',
                  {'subscribers': subscribers})
