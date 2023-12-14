from django.shortcuts import get_object_or_404, render, redirect

from cart.forms import CartAddProductForm

from benches.models import Bench
from .forms import BenchForm

def create_bench(request):
    if request.method == 'POST':
        bench_form = BenchForm(request.POST, request.FILES)
    
        if bench_form.is_valid():
            bench = bench_form.save(commit=False)
            bench.author = request.user  # Устанавливаем автора скамейки текущим пользователем
            bench.save()

            return redirect('mySite:index')  # Укажите URL, куда перенаправить после успешного создания
    else:
        bench_form = BenchForm()

    return render(request, 'benches/create_bench.html', {'bench_form': bench_form})


def bench_list(request):
    benches = Bench.objects.all()
    return render(request, 'mySite:index', {'benches': benches})


def bench_detail(request, bench_id):
    product = get_object_or_404(Bench,
                                id=bench_id,)
    cart_product_form = CartAddProductForm()
    return render(request, 'benches/bench_detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})