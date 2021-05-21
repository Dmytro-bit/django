from django.shortcuts import render
from .forms import JournalForm
from .models import Journal
def journal_logs(request):
    message = ''
    if request.method == "POST":
        form = JournalForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            text = cd['text']
            job = Journal.objects.create(text = text)
            message = f'ваше повідомлення "{text}" записано'
    else:
        form = JournalForm()
    return render(request, 'journal/journal.html', {'form':form, 'message':message})



