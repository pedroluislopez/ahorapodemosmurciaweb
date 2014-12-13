from django.shortcuts import render, get_object_or_404
from blog.models import Publicacion

# Create your views here.
def index(request, num_page=0):
    ENTRIES_PER_PAGE = 4
    num_page = int(num_page)
    entry_count = Publicacion.objects.count()
    max_pages = entry_count / 4
    if num_page < 0:
        num_page = 0
    if num_page > max_pages:
        num_page = max_pages
    offset = num_page * ENTRIES_PER_PAGE
    limit = offset + ENTRIES_PER_PAGE
    print str(offset) + ':' + str(limit)
    
    num_prev = None
    if num_page > 0:
        num_prev = num_page - 1
    num_next = None
    if entry_count > limit:
        num_next = num_page + 1
    
    publicaciones = Publicacion.objects.order_by('-publicado')[offset:limit]
    
    return render(request, 'blog/index.html', {
        'page': 'blog',
        'publicaciones': publicaciones,
        'num_prev': num_prev,
        'num_next': num_next,
    })

def post(request, slug):
    post = get_object_or_404(Publicacion, slug=slug)
    return render(request, 'blog/post.html', {
        'page': 'blog',
        'post': post,
    })
