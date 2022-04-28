from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about-us.html')

def contact(request):
    return render(request, 'main/contact.html')

def service(request):
    return render(request, 'main/service.html')

def item1(request):
    return render(request, 'main/item/item1.html')

def item2(request):
    return render(request, 'main/item/item2.html')

def item3(request):
    return render(request, 'main/item/item3.html')

def item4(request):
    return render(request, 'main/item/item4.html')

def item5(request):
    return render(request, 'main/item/item5.html')

def item6(request):
    return render(request, 'main/item/item6.html')

def item7(request):
    return render(request, 'main/item/item7.html')

def item8(request):
    return render(request, 'main/item/item8.html')

def item9(request):
    return render(request, 'main/item/item9.html')

def item10(request):
    return render(request, 'main/item/item10.html')

def item11(request):
    return render(request, 'main/item/item11.html')

def item12(request):
    return render(request, 'main/item/item12.html')

def item13(request):
    return render(request, 'main/item/item13.html')

def item14(request):
    return render(request, 'main/item/item14.html')

def item15(request):
    return render(request, 'main/item/item15.html')



