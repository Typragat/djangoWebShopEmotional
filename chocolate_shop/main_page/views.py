from django.shortcuts import render
from .forms import SubscribersForm
from products.models import Product, ProductImage
from .emotions_algo import *
import cv2

# Create your views here.

def landing(request):
    name = 'coding'
    current_day = '18.11.2022'
    form = SubscribersForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'index.html', locals())

def home(request):
    cap = cv2.VideoCapture(0)
    success, img = cap.read()
    res = face_analize(img)
    if res[0]['dominant_emotion'] == "happy":
        return render(request, 'happy_face.html')
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    products_images_phones = ProductImage.objects.filter(product__category__id=3)
    products_images_laptops =  ProductImage.objects.filter(product__category__id=2)
    return render(request, 'home.html', locals())
