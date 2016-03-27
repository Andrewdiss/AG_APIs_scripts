from django.shortcuts import render
from education.models import Document


def index(request):
    """ View for index.html

    Return list 'person_education'

    """
    doc_list = Document.objects.all()
    query = request.GET.get("q")
    if query:
        doc_list = doc_list.filter(person_education__icontains=query)
    context = {
        "doc_list": doc_list,
        }
    return render(request, "education/index.html", context)
