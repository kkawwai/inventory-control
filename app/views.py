from django.shortcuts import render, redirect
from django.views import generic
from .models import Product, Branch_one, Branch_three, Branch_two, Central_product
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime, timedelta
# Create your views here.



#倉庫の在庫(classificationごとに分かれて表示される)
class List_WarehouseView(generic.ListView):
    model = Product
    template_name = 'warehouse.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['product_vegetable_list'] = Product.objects.filter(classification='野菜')
        context['product_meet_list'] = Product.objects.filter(classification='肉類')
        context['product_fruits_list'] = Product.objects.filter(classification='フルーツ')
        context['product_seasoning_list'] = Product.objects.filter(classification='調味料')
        context['product_others_list'] = Product.objects.filter(classification='その他')
        
        product_vegetable_paginator = Paginator(context['product_vegetable_list'], 10)
        product_vegetable_page_number = self.request.GET.get('product_vegetable_page')
        product_vegetable_page_obj = product_vegetable_paginator.get_page(product_vegetable_page_number)
        context['product_vegetable_page_obj'] = product_vegetable_page_obj
        
        product_meet_paginator = Paginator(context['product_meet_list'], 10)
        product_meet_page_number = self.request.GET.get('product_meet_page')
        product_meet_page_obj = product_meet_paginator.get_page(product_meet_page_number)
        context['product_meet_page_obj'] = product_meet_page_obj
        
        product_fruits_paginator = Paginator(context['product_fruits_list'], 10)
        product_fruits_page_number = self.request.GET.get('product_fruits_page')
        product_fruits_page_obj = product_fruits_paginator.get_page(product_fruits_page_number)
        context['product_fruits_page_obj'] = product_fruits_page_obj
        
        product_seasoning_paginator = Paginator(context['product_seasoning_list'], 10)
        product_seasoning_page_number = self.request.GET.get('product_seasoning_page')
        product_seasoning_page_obj = product_seasoning_paginator.get_page(product_seasoning_page_number)
        context['product_seasoning_page_obj'] = product_seasoning_page_obj
        
        product_others_paginator = Paginator(context['product_others_list'], 10)
        product_others_page_number = self.request.GET.get('product_others_page')
        product_others_page_obj = product_others_paginator.get_page(product_others_page_number)
        context['product_others_page_obj'] = product_others_page_obj
        
        return context




#支店1の在庫(classificationごとに分かれて表示される)
class List_OneView(generic.ListView):
    model = Branch_one
    template_name = 'branch_one.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['branch_one_vegetable_list'] = Branch_one.objects.filter(classification='野菜')
        context['branch_one_meet_list'] = Branch_one.objects.filter(classification='肉類')
        context['branch_one_fruits_list'] = Branch_one.objects.filter(classification='フルーツ')
        context['branch_one_seasoning_list'] = Branch_one.objects.filter(classification='調味料')
        context['branch_one_others_list'] = Branch_one.objects.filter(classification='その他')
        
        branch_one_vegetable_paginator = Paginator(context['branch_one_vegetable_list'], 10)
        branch_one_vegetable_page_number = self.request.GET.get('branch_one_vegetable_page')
        branch_one_vegetable_page_obj = branch_one_vegetable_paginator.get_page(branch_one_vegetable_page_number)
        context['branch_one_vegetable_page_obj'] = branch_one_vegetable_page_obj
        
        branch_one_meet_paginator = Paginator(context['branch_one_meet_list'], 10)
        branch_one_meet_page_number = self.request.GET.get('branch_one_meet_page')
        branch_one_meet_page_obj = branch_one_meet_paginator.get_page(branch_one_meet_page_number)
        context['branch_one_meet_page_obj'] = branch_one_meet_page_obj
        
        branch_one_fruits_paginator = Paginator(context['branch_one_fruits_list'], 10)
        branch_one_fruits_page_number = self.request.GET.get('branch_one_fruits_page')
        branch_one_fruits_page_obj = branch_one_fruits_paginator.get_page(branch_one_fruits_page_number)
        context['branch_one_fruits_page_obj'] = branch_one_fruits_page_obj
        
        branch_one_seasoning_paginator = Paginator(context['branch_one_seasoning_list'], 10)
        branch_one_seasoning_page_number = self.request.GET.get('branch_one_seasoning_page')
        branch_one_seasoning_page_obj = branch_one_seasoning_paginator.get_page(branch_one_seasoning_page_number)
        context['branch_one_seasoning_page_obj'] = branch_one_seasoning_page_obj
        
        branch_one_others_paginator = Paginator(context['branch_one_others_list'], 10)
        branch_one_others_page_number = self.request.GET.get('branch_one_others_page')
        branch_one_others_page_obj = branch_one_others_paginator.get_page(branch_one_others_page_number)
        context['branch_one_others_page_obj'] = branch_one_others_page_obj
        
        return context



#支店2の在庫(classificationごとに分かれて表示される)
class List_TwoView(generic.ListView):
    model = Branch_two
    template_name = 'branch_two.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['branch_two_vegetable_list'] = Branch_two.objects.filter(classification='野菜')
        context['branch_two_meet_list'] = Branch_two.objects.filter(classification='肉類')
        context['branch_two_fruits_list'] = Branch_two.objects.filter(classification='フルーツ')
        context['branch_two_seasoning_list'] = Branch_two.objects.filter(classification='調味料')
        context['branch_two_others_list'] = Branch_two.objects.filter(classification='その他')
        
        
        branch_two_vegetable_paginator = Paginator(context['branch_two_vegetable_list'], 10)
        branch_two_vegetable_page_number = self.request.GET.get('branch_two_vegetable_page')
        branch_two_vegetable_page_obj = branch_two_vegetable_paginator.get_page(branch_two_vegetable_page_number)
        context['branch_two_vegetable_page_obj'] = branch_two_vegetable_page_obj
        
        branch_two_meet_paginator = Paginator(context['branch_two_meet_list'], 10)
        branch_two_meet_page_number = self.request.GET.get('branch_two_meet_page')
        branch_two_meet_page_obj = branch_two_meet_paginator.get_page(branch_two_meet_page_number)
        context['branch_two_meet_page_obj'] = branch_two_meet_page_obj
        
        branch_two_fruits_paginator = Paginator(context['branch_two_fruits_list'], 10)
        branch_two_fruits_page_number = self.request.GET.get('branch_two_fruits_page')
        branch_two_fruits_page_obj = branch_two_fruits_paginator.get_page(branch_two_fruits_page_number)
        context['branch_two_fruits_page_obj'] = branch_two_fruits_page_obj
        
        branch_two_seasoning_paginator = Paginator(context['branch_two_seasoning_list'], 10)
        branch_two_seasoning_page_number = self.request.GET.get('branch_two_seasoning_page')
        branch_two_seasoning_page_obj = branch_two_seasoning_paginator.get_page(branch_two_seasoning_page_number)
        context['branch_two_seasoning_page_obj'] = branch_two_seasoning_page_obj
        
        branch_two_others_paginator = Paginator(context['branch_two_others_list'], 10)
        branch_two_others_page_number = self.request.GET.get('branch_two_others_page')
        branch_two_others_page_obj = branch_two_others_paginator.get_page(branch_two_others_page_number)
        context['branch_two_others_page_obj'] = branch_two_others_page_obj
        
        return context



#支店3の在庫(classificationごとに分かれて表示される)
class List_ThreeView(generic.ListView):
    model = Branch_three
    template_name = 'branch_three.html'
    
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['branch_three_vegetable_list'] = Branch_three.objects.filter(classification='野菜')
        context['branch_three_meet_list'] = Branch_three.objects.filter(classification='肉類')
        context['branch_three_fruits_list'] = Branch_three.objects.filter(classification='フルーツ')
        context['branch_three_seasoning_list'] = Branch_three.objects.filter(classification='調味料')
        context['branch_three_others_list'] = Branch_three.objects.filter(classification='その他')
        
        
        branch_three_vegetable_paginator = Paginator(context['branch_three_vegetable_list'], 10)
        branch_three_vegetable_page_number = self.request.GET.get('branch_three_vegetable_page')
        branch_three_vegetable_page_obj = branch_three_vegetable_paginator.get_page(branch_three_vegetable_page_number)
        context['branch_three_vegetable_page_obj'] = branch_three_vegetable_page_obj
        
        branch_three_meet_paginator = Paginator(context['branch_three_meet_list'], 10)
        branch_three_meet_page_number = self.request.GET.get('branch_three_meet_page')
        branch_three_meet_page_obj = branch_three_meet_paginator.get_page(branch_three_meet_page_number)
        context['branch_three_meet_page_obj'] = branch_three_meet_page_obj
        
        branch_three_fruits_paginator = Paginator(context['branch_three_fruits_list'], 10)
        branch_three_fruits_page_number = self.request.GET.get('branch_three_fruits_page')
        branch_three_fruits_page_obj = branch_three_fruits_paginator.get_page(branch_three_fruits_page_number)
        context['branch_three_fruits_page_obj'] = branch_three_fruits_page_obj
        
        branch_three_seasoning_paginator = Paginator(context['branch_three_seasoning_list'], 10)
        branch_three_seasoning_page_number = self.request.GET.get('branch_three_seasoning_page')
        branch_three_seasoning_page_obj = branch_three_seasoning_paginator.get_page(branch_three_seasoning_page_number)
        context['branch_three_seasoning_page_obj'] = branch_three_seasoning_page_obj
        
        branch_three_others_paginator = Paginator(context['branch_three_others_list'], 10)
        branch_three_others_page_number = self.request.GET.get('branch_three_others_page')
        branch_three_others_page_obj = branch_three_others_paginator.get_page(branch_three_others_page_number)
        context['branch_three_others_page_obj'] = branch_three_others_page_obj
        
        return context



#セントラルキッチンの在庫(classificationごとに分かれて表示される)
class List_CentralView(generic.ListView):
    model = Central_product
    template_name = 'central.html'
    
    half_year_ago = datetime.now() - timedelta(days=180)
    Product.objects.filter(created_at__lt=half_year_ago).delete()
    Branch_one.objects.filter(created_at__lt=half_year_ago).delete()
    Branch_two.objects.filter(created_at__lt=half_year_ago).delete()
    Branch_three.objects.filter(created_at__lt=half_year_ago).delete()
    Central_product.objects.filter(created_at__lt=half_year_ago).delete()


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['central_product_vegetable_list'] = Central_product.objects.filter(classification='野菜')
        context['central_product_meet_list'] = Central_product.objects.filter(classification='肉類')
        context['central_product_fruits_list'] = Central_product.objects.filter(classification='フルーツ')
        context['central_product_seasoning_list'] = Central_product.objects.filter(classification='調味料')
        context['central_product_others_list'] = Central_product.objects.filter(classification='その他')
        
        
        central_product_vegetable_paginator = Paginator(context['central_product_vegetable_list'], 10)
        central_product_vegetable_page_number = self.request.GET.get('central_product_vegetable_page')
        central_product_vegetable_page_obj = central_product_vegetable_paginator.get_page(central_product_vegetable_page_number)
        context['central_product_vegetable_page_obj'] = central_product_vegetable_page_obj
        
        central_product_meet_paginator = Paginator(context['central_product_meet_list'], 10)
        central_product_meet_page_number = self.request.GET.get('central_product_meet_page')
        central_product_meet_page_obj = central_product_meet_paginator.get_page(central_product_meet_page_number)
        context['central_product_meet_page_obj'] = central_product_meet_page_obj
        
        central_product_fruits_paginator = Paginator(context['central_product_fruits_list'], 10)
        central_product_fruits_page_number = self.request.GET.get('central_product_fruits_page')
        central_product_fruits_page_obj = central_product_fruits_paginator.get_page(central_product_fruits_page_number)
        context['central_product_fruits_page_obj'] = central_product_fruits_page_obj
        
        central_product_seasoning_paginator = Paginator(context['central_product_seasoning_list'], 10)
        central_product_seasoning_page_number = self.request.GET.get('central_product_seasoning_page')
        central_product_seasoning_page_obj = central_product_seasoning_paginator.get_page(central_product_seasoning_page_number)
        context['central_product_seasoning_page_obj'] = central_product_seasoning_page_obj
        
        central_product_others_paginator = Paginator(context['central_product_others_list'], 10)
        central_product_others_page_number = self.request.GET.get('central_product_others_page')
        central_product_others_page_obj = central_product_others_paginator.get_page(central_product_others_page_number)
        context['central_product_others_page_obj'] = central_product_others_page_obj
        
        return context


#トップページ
class ProductListView(generic.ListView):
    template_name = 'index.html'
    paginate_by = 10
    queryset = Product.objects.all().order_by('-classification', 'name', '-created_at')
    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branch_one_list'] = Branch_one.objects.all().order_by('-classification', 'name', '-created_at')
        context['branch_two_list'] = Branch_two.objects.all().order_by('-classification', 'name', '-created_at')
        context['branch_three_list'] = Branch_three.objects.all().order_by('-classification', 'name', '-created_at')
        context['central_list'] = Central_product.objects.all().order_by('-classification', 'name', '-created_at')
        
        branch_one_paginator = Paginator(context['branch_one_list'], 10)
        branch_one_page_number = self.request.GET.get('branch_one_page')
        branch_one_page_obj = branch_one_paginator.get_page(branch_one_page_number)
        context['branch_one_page_obj'] = branch_one_page_obj
        
        branch_two_paginator = Paginator(context['branch_two_list'], 10)
        branch_two_page_number = self.request.GET.get('branch_two_page')
        branch_two_page_obj = branch_two_paginator.get_page(branch_two_page_number)
        context['branch_two_page_obj'] = branch_two_page_obj
        
        branch_three_paginator = Paginator(context['branch_three_list'], 10)
        branch_three_page_number = self.request.GET.get('branch_three_page')
        branch_three_page_obj = branch_three_paginator.get_page(branch_three_page_number)
        context['branch_three_page_obj'] = branch_three_page_obj
        
        central_paginator = Paginator(context['central_list'], 10)
        central_page_number = self.request.GET.get('central_page')
        central_page_obj = central_paginator.get_page(central_page_number)
        context['central_page_obj'] = central_page_obj

        return context



# 商品を倉庫に追加する
def CreateView(request):
    if request.method == 'POST':
        name = request.POST['name']
        weight = int(request.POST['weight'])
        stock = int(request.POST['stock'])
        cost = int(request.POST['cost'])
        classification = request.POST.get('classification')
        
        new_product = Product(name=name, weight=weight, stock=stock, cost=cost, classification=classification)
        new_product.save()
        return redirect('app:product_view')



# 倉庫内にある商品を各支店に送る(トップページから)
def More_Deli(request):
    if request.method == 'POST':
        name = request.POST['name']
        stock = int(request.POST['stock'])
        choice = request.POST.get('product')
        products = Product.objects.filter(name=name)
        
        if not products.exists():
            messages.error(request, '指定された商品が存在しません')
            return redirect('app:product_view')
        
        total_stock = 0
        for product in products:
            total_stock += int(product.stock)

        k = stock
        if total_stock >= k:
            for product in products:
                if product.stock <= k:
                    k = k - product.stock
                    product.delete()
                else:
                    product.stock  -= k
                    product.save()
        else:
            messages.error(request, '数量が在庫の数を超えています')
            return redirect('app:product_view')

        if choice == 'Branch_one':
            try:
                branch_product = Branch_one.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Branch_one.DoesNotExist:
                new_branch_product = Branch_one(name=name, weight=product.weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save()

        elif choice == 'Branch_two': 
            try:
                branch_product = Branch_two.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Branch_two.DoesNotExist:
                new_branch_product = Branch_two(name=name, weight=product.weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save() 

        elif choice == 'Branch_three':
            try:
                branch_product = Branch_three.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Branch_three.DoesNotExist:
                new_branch_product = Branch_three(name=name, weight=product.weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save() 

        elif choice == 'Central_product':
            try:
                branch_product = Central_product.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Central_product.DoesNotExist:
                new_branch_product = Central_product(name=name, weight=product.weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save() 

        else:
            return redirect('app:product_view')
        return redirect('app:product_view')

    else:
        products = Product.objects.all()
        context = {'object_list': products}
        return render(request, 'index.html', context)



# 倉庫内にある商品を各支店に送る(werahouse_listから)
def Send_Deli(request):
    if request.method == 'POST':
        name = request.POST['name']
        stock = int(request.POST['stock'])
        choice = request.POST.get('product')
        products = Product.objects.filter(name=name)
        
        if not products.exists():
            messages.error(request, '指定された商品が存在しません')
            return redirect('app:list_warehouse')
        
        total_stock = 0
        for product in products:
            total_stock += int(product.stock)

        k = stock
        if total_stock >= k:
            for product in products:
                if product.stock <= k:
                    k = k - product.stock
                    product.delete()
                else:
                    product.stock  -= k
                    product.save()
        else:
            messages.error(request, '数量が在庫の数を超えています')
            return redirect('app:list_warehouse')

        if choice == 'Branch_one':
            try:
                branch_product = Branch_one.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Branch_one.DoesNotExist:
                new_branch_product = Branch_one(name=name, weight=product.weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save()

        elif choice == 'Branch_two': 
            try:
                branch_product = Branch_two.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Branch_two.DoesNotExist:
                new_branch_product = Branch_two(name=name, weight=product.weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save() 

        elif choice == 'Branch_three':
            try:
                branch_product = Branch_three.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Branch_three.DoesNotExist:
                new_branch_product = Branch_three(name=name, weight=product.weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save() 

        elif choice == 'Central_product':
            try:
                branch_product = Central_product.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Central_product.DoesNotExist:
                new_branch_product = Central_product(name=name, weight=product.weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save() 

        else:
            return redirect('app:list_warehouse')
        return redirect('app:list_warehouse')

    else:
        products = Product.objects.all()
        context = {'object_list': products}
        return render(request, 'werahouse.html', context)


# 日付を指定してその範囲内のそれぞれの在庫数を表示する
class List_Search_View(generic.ListView):
    model = Product
    template_name = 'datetime.html'
    
    
    def post(self, request, *args, **kwargs):
        
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        choice = request.POST.get('product')

        if choice == 'Product':
            my_objects = Product.objects.filter(created_at__range=[start_date, end_date]).order_by('-created_at')
            context = {'my_objects': my_objects}

        elif choice == 'Branch_one':
            my_objects = Branch_one.objects.filter(created_at__range=[start_date, end_date]).order_by('-created_at')
            context = {'my_objects': my_objects}

        elif choice == 'Branch_two':
            my_objects = Branch_two.objects.filter(created_at__range=[start_date, end_date]).order_by('-created_at')
            context = {'my_objects': my_objects}

        elif choice == 'Branch_three':
            my_objects = Branch_three.objects.filter(created_at__range=[start_date, end_date]).order_by('-created_at')
            context = {'my_objects': my_objects}

        elif choice == 'Central_product':
            my_objects = Central_product.objects.filter(created_at__range=[start_date, end_date]).order_by('-created_at')
            context = {'my_objects': my_objects}

        else:
            my_objects = Product.objects.filter(created_at__range=[start_date, end_date])
            context = {'my_objects': my_objects}
        
        return render(request, 'datetime.html', context)



#支店1の商品を使用し在庫を減らす
def Liquidation_one_View(request):
    if request.method == 'POST':
        name = request.POST['name']
        stock = int(request.POST['stock'])
        objects = Branch_one.objects.filter(name=name).order_by('created_at')
        
        
        if not objects.exists():
            messages.error(request, '指定された商品が存在しません')
            return redirect('app:list_one')

        k = stock
        total = 0
        for object in objects:
            total += int(object.stock)

        if total < k:
            messages.error(request, 'ERROR 在庫の数よりも多いです')
            return redirect('app:list_one')
        else:
            for object in objects:
                if object.stock > k:
                    if k > 0:
                        object.stock = object.stock - k
                        object.save()
                    else:
                        redirect('app:list_one')
                elif object.stock == k:
                    object.delete()
                else:
                    k -= object.stock
                    object.delete()
            return redirect('app:list_one')


#支店2の商品を使用し在庫を減らす
def Liquidation_two_View(request):
    if request.method == 'POST':
        name = request.POST['name']
        stock = int(request.POST['stock'])
        objects = Branch_two.objects.filter(name=name).order_by('created_at')
        
        if not objects.exists():
            messages.error(request, '指定された商品が存在しません')
            return redirect('app:list_two')
        
        k = stock
        total = 0
        for object in objects:
            total += int(object.stock)

        if total < k:
            messages.error(request, 'ERROR 在庫の数よりも多いです')
            return redirect('app:list_two')
        else:
            for object in objects:
                if object.stock > k:
                    if k > 0:
                        object.stock = object.stock - k
                        object.save()
                    else:
                        redirect('app:list_two')
                elif object.stock == k:
                    object.delete()
                else:
                    k -= object.stock
                    object.delete()
            return redirect('app:list_two')
        
        

#支店3の商品を使用し在庫を減らす
def Liquidation_three_View(request):
    if request.method == 'POST':
        name = request.POST['name']
        stock = int(request.POST['stock'])
        objects = Branch_three.objects.filter(name=name).order_by('created_at')
        
        if not objects.exists():
            messages.error(request, '指定された商品が存在しません')
            return redirect('app:list_three')
        
        k = stock
        total = 0
        for object in objects:
            total += int(object.stock)

        if total < k:
            messages.error(request, 'ERROR 在庫の数よりも多いです')
            return redirect('app:list_three')
        else:
            for object in objects:
                if object.stock > k:
                    if k > 0:
                        object.stock = object.stock - k
                        object.save()
                    else:
                        redirect('app:list_three')
                elif object.stock == k:
                    object.delete()
                else:
                    k -= object.stock
                    object.delete()
            return redirect('app:list_three')
        
        
        
#セントラルキッチンの商品を使用し在庫を減らす
def Liquidation_central_View(request):
    if request.method == 'POST':
        name = request.POST['name']
        stock = int(request.POST['stock'])
        objects = Central_product.objects.filter(name=name).order_by('created_at')
        
        if not objects.exists():
            messages.error(request, '指定された商品が存在しません')
            return redirect('app:list_central')
        
        k = stock
        total = 0
        for object in objects:
            total += int(object.stock)

        if total < k:
            messages.error(request, 'ERROR 在庫の数よりも多いです')
            return redirect('app:list_central')
        else:
            for object in objects:
                if object.stock > k:
                    if k > 0:
                        object.stock = object.stock - k
                        object.save()
                    else:
                        redirect('app:list_central')
                elif object.stock == k:
                    object.delete()
                else:
                    k -= object.stock
                    object.delete()
            return redirect('app:list_central')