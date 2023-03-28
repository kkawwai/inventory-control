
"""
def More_Deli(request):
    form = MoreDeliForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        stock = int(form.cleaned_data['stock'])
        weight = int(form.cleaned_data['weight'])
        choice = form.cleaned_data['choice']
        products = Product.objects.filter(name=name)
        k = stock
        for product in products:
            if product.stock <= k:
                k = k - product.stock
                product.delete()
            else:
                product.stock  -= k
                product.save()
    
        if choice == 'Branch_one':
            try:
                branch_product = Branch_one.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Branch_one.DoesNotExist:
            # Branch_one モデルに新しい商品を追加する
                new_branch_product = Branch_one(name=name, weight=weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save()
        
        elif choice == 'Branch_two': 
            try:
                branch_product = Branch_two.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Branch_two.DoesNotExist:
            # Branch_one モデルに新しい商品を追加する
                new_branch_product = Branch_two(name=name, weight=weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save() 
        elif choice == 'Branch_three':
            try:
                branch_product = Branch_three.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Branch_three.DoesNotExist:
            # Branch_one モデルに新しい商品を追加する
                new_branch_product = Branch_three(name=name, weight=weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save() 
        elif choice == 'Central_product':
            try:
                branch_product = Central_product.objects.get(name=name)
                branch_product.stock += stock
                branch_product.save()
            except Central_product.DoesNotExist:
            # Branch_one モデルに新しい商品を追加する
                new_branch_product = Central_product(name=name, weight=weight, stock=stock, cost=product.cost, classification=product.classification)
                new_branch_product.save() 
        else:
            return redirect('app:index')
        return redirect('app:index')
    else:
        products = Product.objects.all()
        total = 0
        for product in products:
            total += product.stock * product.cost
        context = {'object_list': products, 'total': total, 'form':form}
        return render(request, 'more_deli.html', context)
"""







"""   
class ProductListView(generic.ListView):
    model = Product
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # nameが同じオブジェクトのstockを合計する
        queryset = queryset.values('name').annotate(total_stock=models.Sum('stock'))
        queryset = queryset.values('name', 'total_stock', 'weight', 'cost', 'classification', 'updated_at')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unique_products = {}
        for product in context['object_list']:
            if product['name'] not in unique_products:
                unique_products[product['name']] = product
            else:
                unique_products[product['name']]['total_stock'] += product['total_stock']
        context['object_list'] = unique_products.values()
        return context
"""


"""
class ProductListView(generic.ListView):
    model = Product
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # nameが同じオブジェクトのstockを合計する
        queryset = queryset.values('name').annotate(total_stock=models.Sum('stock'))
        queryset = queryset.values('name', 'total_stock', 'weight', 'cost', 'classification', 'updated_at')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unique_products = {}
        for product in context['object_list']:
            if product['name'] not in unique_products:
                unique_products[product['name']] = product
            else:
                unique_products[product['name']]['total_stock'] += product['total_stock']
        context['object_list'] = unique_products.values()
        return context
        
        
        def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unique_products = {}
        for product in context['object_list']:
            if product['name'] not in unique_products:
                unique_products[product['name']] = product
            else:
                unique_products[product['name']]['total_stock'] += product['total_stock']
        context['object_list'] = unique_products.values()
        return context
"""


"""
class ProductListView(generic.ListView):
    model = Product
    template_name = 'index.html'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-classification', 'name', '-created_at')
        
        return queryset

"""

"""
def index(request):
    if request.method == 'POST':
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

    else:
        return render(request, 'datetime.html')

"""

"""
half_year_ago = datetime.now() - timedelta(days=180)
    Product.objects.filter(created_at__lt=half_year_ago).delete()
    Branch_one.objects.filter(created_at__lt=half_year_ago).delete()
    Branch_two.objects.filter(created_at__lt=half_year_ago).delete()
    Branch_three.objects.filter(created_at__lt=half_year_ago).delete()
    Central_product.objects.filter(created_at__lt=half_year_ago).delete()

"""

"""
self.kwargs['my_objects'] = context['my_objects']
"""