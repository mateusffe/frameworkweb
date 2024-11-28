from django.shortcuts import render, get_object_or_404
from .models import *
import requests

from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    return render(request, 'index.html')


def pesquisa(request):
    query = request.GET.get('q', '')  
    resultados = Pessoa.objects.filter(nome__icontains=query)  
    return render(request, 'pesquisa.html', {'resultados': resultados, 'query': query})

def pessoa(request, id):
    contexto = get_object_or_404(Pessoa, pk=id)
    
    nome = contexto.nome
    noticias = []
    
    try:
        # URL de pesquisa no Google News
        url = f'https://news.google.com/search?q={nome}&hl=pt-BR&gl=BR&ceid=BR:pt-419'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Selecionar as notícias (exemplo baseado na estrutura do Google News)
        for item in soup.select('article'):
            titulo_tag = item.select_one('a.JtKRv')  # Seleciona a tag <a> com a classe JtKRv
            titulo = titulo_tag.get_text(strip=True) if titulo_tag else "Sem título"
            link = f"https://news.google.com{item.a['href'][1:]}" if item.a else "#"
            noticias.append({'titulo': titulo, 'link': link})
    except Exception as e:
        print(f"Erro ao buscar notícias: {e}")
    
    # Passar o contexto para o template
    return render(request, 'pessoa.html', {'pessoa': contexto, 'noticias': noticias})
