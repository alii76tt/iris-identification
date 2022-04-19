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

    if 'setosa' in prediction:
        image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/640px-Irissetosa1.jpg"
    elif 'versicolor' in prediction:
        image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a8/Iris_versicolor_5zz.jpg"
    else:
        image_url = "https://upload.wikimedia.org/wikipedia/commons/2/27/Southern_Blue_Flag_Iris_%28iris_virginica%29_-_Flickr_-_Andrea_Westmoreland.jpg"
    
    context = {
        'prediction': prediction,
        'image_url': image_url
    }
    return render(request, 'index.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
