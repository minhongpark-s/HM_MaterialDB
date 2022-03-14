from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth.decorators import login_required
from common.decorators import allowed_users

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            studentNumber = request.POST['studentNumber']
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('DBshow:main')
    else:
        form = UserForm()
    return render(request, 'common/templates/common/signup.html', {'form': form})

@login_required(login_url='common:login')
@allowed_users(allowed_roles=['하이멕 관리부원','하이멕 일반부원'])
def okok(request):
    return render(request, 'common/templates/common/okok.html')
    
def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})