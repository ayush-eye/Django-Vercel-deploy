from django.shortcuts import render, redirect

def set_preference(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        theme = request.POST.get('theme')

        response = redirect('show_preference')
        response.set_cookie('language', language, max_age=3600)
        response.set_cookie('theme', theme, max_age=3600)
        return response

    return render(request, 'userprefs/set_pref.html')


def show_preference(request):
    language = request.COOKIES.get('language', 'Not Set')
    theme = request.COOKIES.get('theme', 'Not Set')

    return render(request, 'userprefs/show_pref.html', {
        'language': language,
        'theme': theme
    })
