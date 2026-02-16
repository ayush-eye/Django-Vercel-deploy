from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    form = FeedbackForm()
    submitted = False

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            submitted = True

    return render(request, "feedback.html", {
        'form': form,
        'submitted': submitted
    })
