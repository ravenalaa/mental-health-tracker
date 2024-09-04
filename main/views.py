from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275355',
        'name': 'Claudia Paskalia Koesno',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)