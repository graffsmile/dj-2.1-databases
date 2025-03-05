from django.shortcuts import render, redirect
from phones.models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    phones_list = []
    for phone in phones:
        phones_list.append(
            {
                'name': phone.name,
                'price': round(phone.price, 2),
                'image': phone.image,
                'slug': phone.slug
            }
        )
    sort = request.GET.get('sort')
    if sort == 'name':
        phones_list.sort(key=lambda value: value['name'])
    elif sort == 'min_price':
        phones_list.sort(key=lambda value: value['price'])
    elif sort == 'max_price':
        phones_list.sort(key=lambda value: value['price'], reverse=True)
    else:
        pass

    context = {
        'phones': phones_list,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
