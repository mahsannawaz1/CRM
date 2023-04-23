from django.http import HttpResponse
from django.shortcuts import redirect, render


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():

                count = request.user.groups.all().count()
                flag = 0
                if count == 0:
                    return render(request, 'customer/unauthorized.html')

                else:
                    group = request.user.groups.all().values('name')
                    groups = list(group)
                    for i in range(0, count):

                        if groups[i]['name'] in allowed_roles:
                            flag = 1
                            break
                    if flag == 1:
                        return view_func(request, *args, **kwargs)
                    elif flag == 0:
                        return render(request, 'customer/unauthorized.html')
            else:
                return render(request, 'customer/unauthorized.html')
        return wrapper_func
    return decorator
