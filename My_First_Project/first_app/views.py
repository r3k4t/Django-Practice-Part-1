from django.shortcut import render
from django.http  import HttpResponse 
from first_app.models import Musician,Album


def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1':' List of Musicians','musician':muscian_list}
    return render(request,'first_app/index.html',context=diction)