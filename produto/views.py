from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Produto, Categoria, Adicional, Opcoes  # Import the Produto, Categoria, Adicional, and Opcoes models
from django.contrib.auth.decorators import login_required

def home(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()

    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()

    # Simulação: os 4 primeiros como mais vendidos e promoções
    mais_vendidos = Produto.objects.filter(ativo=True)[:4]
    promocoes = Produto.objects.filter(ativo=True).order_by('-id')[:3]

    return render(request, 'home.html', {
        'produtos': produtos,
        'carrinho': len(request.session['carrinho']),
        'categorias': categorias,
        'mais_vendidos': mais_vendidos,
        'promocoes': promocoes,
    })

def categorias(request, id):
    produtos = Produto.objects.filter(categoria_id = id)
    categorias = Categoria.objects.all()

    return render(request, 'home.html', {'produtos': produtos,
                                        'carrinho': len(request.session['carrinho']),
                                        'categorias': categorias,})

def produto(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    erro = request.GET.get('erro')
    produto = Produto.objects.filter(id=id)[0]
    categorias = Categoria.objects.all()
    return render(request, 'produto.html', {'produto': produto, 
                                            'carrinho': len(request.session['carrinho']),
                                            'categorias': categorias,
                                            'erro': erro})

def add_carrinho(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()

    x = dict(request.POST)
    def removeLixo():
        adicionais = x.copy()
        adicionais.pop('id')
        adicionais.pop('csrfmiddlewaretoken')
        adicionais.pop('observacoes')
        adicionais.pop('quantidade')
        adicionais = list(adicionais.items())

        return adicionais
        
    adicionais = removeLixo()  
    id = int(x['id'][0])
    preco_total = Produto.objects.filter(id=id)[0].preco
    adicionais_verifica =  Adicional.objects.filter(produto = id)
    aprovado = True
    for i in adicionais_verifica:
        encontrou = False
        minimo = i.minimo
        maximo = i.maximo
        for j in adicionais:
            if i.nome == j[0]:
                encontrou = True
                if len(j[1]) < minimo or len(j[1]) > maximo:
                    aprovado = False
        if minimo > 0 and not encontrou:
            aprovado = False
    
    if not aprovado:
        return redirect(f'/produto/{id}?erro=1')
        
    for i, j in adicionais:
        for k in j:
            preco_total += Opcoes.objects.filter(id=int(k))[0].acrecimo

    def troca_id_por_nome_adicional(adicional):
        adicionais_com_nome = []
        for i in adicionais:
            opcoes = []
            for j in i[1]:
                op = Opcoes.objects.filter(id = int(j))[0].nome
                opcoes.append(op) 
            adicionais_com_nome.append((i[0], opcoes))
        return adicionais_com_nome
    
    adicionais = troca_id_por_nome_adicional(adicionais)

    preco_total *= int(x['quantidade'][0])

    data = {'id_produto': int(x['id'][0]),
            'observacoes': x['observacoes'][0],
            'preco': preco_total,
            'adicionais': adicionais,
            'quantidade': x['quantidade'][0]}

    request.session['carrinho'].append(data)
    request.session.save()
    return redirect('/ver_carrinho')

def ver_carrinho(request):
    categorias = Categoria.objects.all()
    dados_motrar = []
    for i in request.session['carrinho']:
        prod = Produto.objects.filter(id=i['id_produto'])
        dados_motrar.append(
            {'imagem': prod[0].img.url,
             'nome': prod[0].nome_produto,
             'quantidade': i['quantidade'],
             'preco': i['preco'],
             'id': i['id_produto']
             }
        )

    total = sum([float(i['preco']) for i in request.session['carrinho']])

    return render(request, 'carrinho.html', {'dados': dados_motrar,
                                             'total': total,
                                             'carrinho': len(request.session['carrinho']),
                                             'categorias': categorias,
                                             })

def remover_carrinho(request, id):
    request.session['carrinho'].pop(id)
    request.session.save()
    return redirect('/ver_carrinho')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('perfil')  # <- vai para o perfil
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'login.html')

from django.contrib.auth.decorators import login_required

def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('cadastro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já está em uso.')
            return redirect('cadastro')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user)  # <- loga automaticamente após cadastro
        return redirect('perfil')  # <- redireciona para o perfil
    
    return render(request, 'cadastro.html')


@login_required
def perfil_view(request):
    return render(request, 'produto/perfil.html')


