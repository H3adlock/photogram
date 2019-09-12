from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import CommentForm
from .models import Post
import time
from django.conf import settings


def get_category_count():
    category_count = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return category_count


def home(request):
    featured = Post.objects.filter(featured=True)[0:5]
    count = 0
    featured_right = list()
    featured_left = list()
    for obj in featured:
        if count == 0:
            featured_right.append(obj)
        elif count % 2 != 0:
            featured_left.append(obj)
        else:
            featured_right.append(obj)
        count += 1

    latest = Post.objects.all().order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        'object_list_left': featured_left,
        'object_list_right': featured_right,
        'latest': latest,
    }
    return render(request, 'index.html', context)


def gallery(request):
    category_count = get_category_count()
    post_list = Post.objects.all().order_by('-timestamp')
    latest = Post.objects.all().order_by('-timestamp')[0:3]
    search = request.GET.get('q')
    if search:
        post_list = post_list.filter(
            Q(title__icontains=search) |
            Q(overview__icontains=search) |
            Q(content__icontains=search)
            # | Q(timestamp__icontains=search)
            # | Q(author__user__icontains=search)
            # | Q(categories__icontains=search)
        ).distinct()
        paginator = Paginator(post_list, 1)
    else:
        paginator = Paginator(post_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'latest': latest,
        'paginated_queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'num_pages': range(1, paginator.num_pages + 1),
        'category_count': category_count,
    }
    return render(request, 'gallery.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'slug': post.slug
            }))
    latest = Post.objects.all().order_by('-timestamp')[0:3]
    category_count = get_category_count()
    context = {
        'form': form,
        'post': post,
        'latest': latest,
        'category_count': category_count,
    }
    return render(request, "post.html", context)


def profile(request, username):
    post = get_object_or_404(Post, slug=slug)
