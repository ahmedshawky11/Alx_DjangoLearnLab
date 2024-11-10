from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.userprofile.role == 'ADMIN'

def admin_view(request):
    if not is_admin(request.user):
        return HttpResponseForbidden()
    # Your admin view logic here
    return render(request, 'admin_view.html')

def is_librarian(user):
    return user.userprofile.role == 'LIBRARIAN'

def librarian_view(request):
    if not is_librarian(request.user):
        return HttpResponseForbidden()
    # Your librarian view logic here
    return render(request, 'librarian_view.html')

def is_member(user):
    return user.userprofile.role == 'MEMBER'

def member_view(request):
    if not is_member(request.user):
        return HttpResponseForbidden()
    # Your member view logic here
    return render(request, 'member_view.html')
