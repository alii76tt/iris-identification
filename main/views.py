from django.shortcuts import render
from .modul import getIris


def index(request):

    if request.method == 'GET':
        sl = request.GET.get('sl')
        sw = request.GET.get('sw')
        pl = request.GET.get('pl')
        pw = request.GET.get('pw')
        if sl and sw and pl and pw:
            try:
                prediction = getIris(sl, sw, pl, pw)
            except ValueError:

                return render(request, "index.html", {
                    "error": "Please enter integer value!", 'prediction': "-"
                })
        else:
            return render(request, "index.html", {
                "error": "Please fill in the fields!", 'prediction': "-"
            })

    prediction = str(prediction).replace("'", "")

    context = {
        'prediction': prediction,
    }
    return render(request, 'index.html', context)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)