from django.shortcuts import render

def home(request):
    return render(request, 'tech-index.html')


def gadgets(request):
    gadgets = Gadgets.objects.all()
    context = {'gadgets':gadgets}
    return render(request, "gadgates/tech-category-01.html", context)


    