from django.shortcuts import render, get_object_or_404, redirect
from .models import Word, Category
from django.db.models import Q
from django.http import JsonResponse


def home(request, slug=None):
    if slug:
        category = get_object_or_404(Category, slug=slug)
        if category.children.exists():
            categories = category.children.all()
            return render(request, 'detail.html', {'categories': categories})
        else:
            return word(request, category.words.first().slug)
    else:
        categories = Category.objects.filter(parent__isnull=True)
        return render(request, 'detail.html', {'categories': categories})


def word(request, slug):
    words = Word.objects.filter(slug=slug)
    if not words:
        return render(request, 'notfinde.html')
    context = {'words': words}

    return render(request, 'home.html', context)


def search(request):
    query = request.GET.get('q')
    words = Word.objects.none()
    if query:
        words = Word.objects.filter(Q(title__icontains=query) | Q(pronunciation__icontains=query))
    context = {'words': words}
    return render(request, 'search.html', context)


def add_to_favorites(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    word.favorite.add(request.user)
    return redirect('home')


def remove_favorites(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    word.favorite.remove(request.user)
    return redirect('home')


def my_favorites(request):
    words = request.user.favorite_words.all()
    context = {'words': words}
    return render(request, 'favorites.html', context)


def autocomplete(request):
    if 'term' in request.GET:
        qs = Word.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for word in qs:
            titles.append(word.title)
        return JsonResponse(titles, safe=False)
    return render(request, 'search.html')
