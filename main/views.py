from django.shortcuts import render
from .models import SaiArts

# Create your views here.

def home_view(request):
    home = SaiArts.objects.all()
    context = {'home': home}
    template = 'main.html'
    return render(request, template, context)


# about section
def about_view(request):
    about = SaiArts.objects.all()
    context = {'about': about}
    template = 'about.html'
    return render(request, template, context)