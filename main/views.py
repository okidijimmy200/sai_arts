from django.shortcuts import render,  get_object_or_404
from .models import SaiArts

# Create your views here.

def home_view(request):
    home = SaiArts.created.all()[:3]
    exibited = SaiArts.exibited.all()[:3]
    context = {'home': home,
                'exibited': exibited}
    template = 'main.html'
    return render(request, template, context)

# lastestPieces all Page

def all_artPieces(request):
    home = SaiArts.created.all()
    context = {'home': home}
    template = 'allArtPieces.html'
    return render(request, template, context)

# all exibited art pieces
def all_exibited(request):
    exibited = SaiArts.exibited.all()
    context = {'exibited': exibited}
    template = 'allExibitedPieces.html'
    return render(request, template, context)

# artPieces detail view
def art_detail(request, artpiece):
    artpiece = get_object_or_404(SaiArts, slug=artpiece)

    return render(request, 'artDetail.html', {'artpiece': artpiece})



# about section
def about_view(request):
    about = SaiArts.objects.all()
    context = {'about': about}
    template = 'about.html'
    return render(request, template, context)