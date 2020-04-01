from urllib.parse import urlencode
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import Product, Topic, Departament, TopicProduct, User
from .forms import UserAuthenticationForm


class StartView(View):
    def get(self, request):
        template = 'app/index1.html'
        topics_products = Topic.objects.all().prefetch_related('product').order_by('-creation_date')
        departaments = Departament.objects.all()
        context = {'objects': topics_products,
                   'departaments': departaments}
        # print(request.session.items())
        return render(request, template, context)

    def post(self, request):
        template = 'app/index1.html'
        topics_products = Topic.objects.all().prefetch_related('product').order_by('-creation_date')
        departaments = Departament.objects.all()
        product_id = request.POST['product_id']
        print(product_id)
        # print(type(product_id))
        # print(a.values('product_id'))

        if 'cart' not in request.session:
            request.session['cart'] = list()
            request.session['cart'].append({'product_id': int(product_id), 'values': 1})
        # else:
        #     for i in request.session['cart']:
        #         if i['product_id'] == int(product_id):
        #             i['values'] += 1
        #         else:
        #             request.session['cart'].append({'product_id': int(product_id), 'values': 1})

        print(request.session['cart'])
        context = {'objects': topics_products,
                   'departaments': departaments}

        return render(request, template, context)


class ProductView(View):
    def get(self, request, slug):
        template = 'app/product.html'
        products = Product.objects.filter(slug_name=slug)
        context = {'products': products}
        return render(request, template, context)

    def post(self, request):
        pass


class CatalogView(View):
    def get(self, request, slug):
        template = 'app/catalog.html'
        product_list = Product.objects.select_related('departament').filter(departament__slug_name=slug)
        print(product_list)

        paginator = Paginator(product_list, 1)
        current_page = request.GET.get('page', 1)
        products = paginator.get_page(current_page)
        prev_page_num, next_page_num = 1, 1
        if products.has_previous():
            prev_page_num = products.previous_page_number()
        if products.has_next():
            next_page_num = products.next_page_number()
        next_page_url = urlencode({'page': next_page_num})
        prev_page_url = urlencode({'page': prev_page_num})

        context = {'products': products,
                   'current_page': products.number,
                   'prev_page_url': f'?{prev_page_url}',
                   'next_page_url': f'?{next_page_url}'}
        return render(request, template, context)


class CartView(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return
            pass
        else:
            pass
