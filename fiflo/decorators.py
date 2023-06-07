from django.http import HttpResponse

def is_allowed(allowed_roles = []):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            print('GROUP: ', request.user.groups.all())
            if request.user.groups.all():
                if str(request.user.groups.all()[0]) in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('Not allowed')
            else:
                return HttpResponse('Not allowed')
        return wrap
    return decorator
    