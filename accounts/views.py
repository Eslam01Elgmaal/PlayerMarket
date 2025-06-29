from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'signup':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                login(request, user)
                messages.success(request, 'تم إنشاء الحساب بنجاح')
                return redirect('home:home_detail')
            else:
                messages.error(request, 'من فضلك راجع البيانات')

        elif action == 'signin':
            username = request.POST.get('login_username')
            password = request.POST.get('login_password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #messages.success(request, 'تم تسجيل الدخول بنجاح')
                return redirect('home:home_detail')
            else:
                messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')

    else:
        form = SignUpForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('auth') 