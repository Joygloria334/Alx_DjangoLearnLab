from django.shortcuts import render
from django.contrib.auth.decorators import ser_passes_test

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user. userprofile.role == 'librarian'
def is_member(user):
    return user.userprofile.role == 'Member'

#Admin view - only admins can access this
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@users_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# Create your views here.
