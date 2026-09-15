import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import Pagevisit

this_dir=pathlib.Path(__file__).resolve().parent


def home_page_view(request , *args , **kwargs):

    Pagevisit.objects.create(path=request.path)
    qs = Pagevisit.objects.all()
    page_qs = Pagevisit.objects.filter(path = request.path)

    my_title="My Page"
    my_context={
        "page_title":my_title,
        "queryset":qs.count(),
        "page_visit_count":page_qs.count(),

        "percent": (page_qs.count()*100.0)/qs.count(),
    }
    html_template = "home.html"
    return render(request , html_template , my_context)




def old_home_page_view(request , *args , **kwargs):
    print(this_dir)

    html=""
    html_file_path= this_dir / "home.html"
    html_ = html_file_path.read_text()

    return HttpResponse(html_)