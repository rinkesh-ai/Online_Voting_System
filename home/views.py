from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context={"home":"active"}
    return render(request, 'index.html', context)
    # return HttpResponse("This is a homePage...")

def contact(request):
    context={"contact":"active"}
    return render(request, 'contact.html', context)

def about(request):
    context={"about":"active"}
    return render(request, 'about.html', context)

def voteInput(request):
    context={"voteInput":"active"}
    return render(request, 'voteInput.html', context)

def finalVote(request):
    context={"finalVote":"active"}
    return render(request, 'finalVote.html', context)
    