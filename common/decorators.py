from django.http import HttpResponse
# 처음 함수는 유저 권한을 받아오는 역할만 한다.
def allowed_users(allowed_roles=[]):
    # 실질적인 데코레이터의 기능은 이 함수가 담당한다.
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('권한이 없습니다.')
        return wrapper_func
    return decorator