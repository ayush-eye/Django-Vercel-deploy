from django.shortcuts import render, redirect

def set_preference(request):
    if request.method == "POST":
        theme = request.POST.get('theme')
        response = redirect('show_preference')
        response.set_cookie('theme', theme)
        return response
    return render(request, 'set_pref.html')

def show_preference(request):
    theme = request.COOKIES.get('theme', 'Not set')
    return render(request, 'show_pref.html', {'theme': theme})
