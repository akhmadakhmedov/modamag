from .models import Category

def menu_links(request):
    links = Category.objects.all()
    linki = Category.objects.all().order_by('-id')[:8]
    return dict(links = links, linki=linki)

