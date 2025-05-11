from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bookmark, Category
from .forms import BookmarkForm, CategoryForm, SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    # Handle add bookmark
    if request.method == 'POST' and 'add_bookmark' in request.POST:
        bookmark_form = BookmarkForm(request.POST)
        if bookmark_form.is_valid():
            bookmark = bookmark_form.save(commit=False)
            bookmark.user = request.user
            bookmark.save()
            messages.success(request, "Bookmark added!")
            return redirect('home')
    else:
        bookmark_form = BookmarkForm()

    # Handle add category
    if request.method == 'POST' and 'add_category' in request.POST:
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Category added!")
            return redirect('home')
    else:
        category_form = CategoryForm()

    # Handle delete bookmark
    if request.method == 'POST' and 'delete_bookmark' in request.POST:
        bookmark_id = request.POST.get('delete_bookmark')
        Bookmark.objects.filter(id=bookmark_id, user=request.user).delete()
        messages.success(request, "Bookmark deleted!")
        return redirect('home')

    # Handle delete category
    if request.method == 'POST' and 'delete_category' in request.POST:
        category_id = request.POST.get('delete_category')
        category = Category.objects.get(id=category_id)
        if category.name != Category.DEFAULT_NAME:
            category.delete()
            messages.success(request, "Category and its bookmarks deleted!")
        else:
            messages.error(request, "Cannot delete the default category.")
        return redirect('home')

    # Filtering bookmarks by category
    categories = Category.objects.all()
    selected_category_id = request.GET.get('category')
    if selected_category_id:
        bookmarks = Bookmark.objects.filter(user=request.user, category_id=selected_category_id)
    else:
        bookmarks = Bookmark.objects.filter(user=request.user)

    context = {
        'bookmarks': bookmarks,
        'categories': categories,
        'selected_category_id': selected_category_id,
        'bookmark_form': bookmark_form,
        'category_form': category_form,
    }
    return render(request, 'home.html', context)
