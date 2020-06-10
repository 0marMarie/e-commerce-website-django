from django.shortcuts import render ,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .forms import Contact
from django.core.mail import send_mail
from .models import Product , Category
from cart.forms import CartAddProduct


# Create your views here.


def index(request):

    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['deva4rf@gmail.com'])
            return HttpResponse('Thanks for contacting us!')
    else:
        form = Contact()

    men = Product.objects.filter(category_id=1).filter(featured=True)
    women = Product.objects.filter(category_id=2).filter(featured=True)
    kids = Product.objects.filter(category_id=3).filter(featured=True)
    acc = Product.objects.filter(category_id=4).filter(featured=True)
    special = Product.objects.filter(special=True)

    context = {
        'form': form,
        'men':men,
        'women':women,
        'kids' : kids,
        'acc':acc,
        'special':special,
        'cart_product_form': CartAddProduct()



    }


    return render(request,'index.html',context)


def cart(request):
    return render(request,'cart.html',{})

def categories(request,slug=None):

    categories = Category.objects.all()
    products = Product.objects.filter(avilable=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': CartAddProduct()
    }
    return render(request, 'cat.html', context)


def product_detail(request, slug , id):


    product = get_object_or_404(Product, id=id, slug=slug , avilable=True)

    context = {
        'product': product,
        'cart_product_form' : CartAddProduct()
    }


    return render(request,'details.html',context)
def search(request):

    query = request.GET.get('q')

    product = Product.objects.filter(

                                      Q(name__icontains=query) |
                                      Q(descp__icontains=query)

                                      )

    context = {
        'query' :query ,
        'cart_product_form': CartAddProduct(),
        'product': product
    }

    return render(request,'results.html',context)

