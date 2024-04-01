import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    site_info = "Привет это мой сайт"
    about_me = "Меня зовут Дмитрий я учусь програмированию"
    
    html = f"""
        <h1>Главная страница</h1>
        <p>{site_info}</p>
        <p>{about_me}</p>
    """
    print("Посещена главная страница")

    return HttpResponse(html)

def about(request):
    site_info = "Это мой первый Django-сайт"
    about_me = "Меня зовут Дмитрий и я начинающий веб-разработчик"

    # HTML-верстка
    html = f"""
        <h1>О себе</h1>
        <p>{site_info}</p>
        <p>{about_me}</p>
    """
    
    # Сохранение в логи данных о посещении страницы
    print("Посещена страница 'О себе'")

    return HttpResponse(html)

# Create your views here.
