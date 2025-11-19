# relationship_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Book, Library, UserProfile


# Existing views
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('list_books')  # Redirect to books list after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


# Helper functions to check user roles
def is_admin(user):
    """Check if user has Admin role"""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    """Check if user has Librarian role"""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    """Check if user has Member role"""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Role-based views
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    """
    View accessible only to users with Admin role.
    """
    context = {
        'user': request.user,
        'role': request.user.userprofile.role
    }
    return render(request, 'relationship_app/admin_view.html', context)


@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    """
    View accessible only to users with Librarian role.
    """
    context = {
        'user': request.user,
        'role': request.user.userprofile.role
    }
    return render(request, 'relationship_app/librarian_view.html', context)


@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    """
    View accessible only to users with Member role.
    """
    context = {
        'user': request.user,
        'role': request.user.userprofile.role
    }
    return render(request, 'relationship_app/member_view.html', context)