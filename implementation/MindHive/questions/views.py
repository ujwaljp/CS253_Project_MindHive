from django.http import HttpResponse

# Create your views here.
def view(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def edit(request, question_id):
    return HttpResponse("You're editing question %s." % question_id)

def ask(request):
    return HttpResponse("You're asking a question.")