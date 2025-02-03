from django.contrib import admin
from django.urls import path, include
from mesas import views as mesas_views  # Alias para las vistas de mesas
from menu import views as menu_views  # Alias para las vistas de menú
from estadisticas import views as estadisticas_views
from menu.views import categories_view, meals_view, convertir_divisa


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mesas_views.home, name='home'),  # Usando alias para vistas de mesas

    path('login/', mesas_views.login_view, name='login'),
    path('register/', mesas_views.register, name='register'),

    path('menu/', menu_views.gestionar_menu, name='gestionar_menu'),  # Usando alias para vistas de menú
    path('estadistica/', estadisticas_views.estadistica, name='estadistica'),
    path('estadisticas/meseros/', estadisticas_views.estadisticas_meseros, name='estadisticas_meseros'),
    path('estadisticas/mesas/', estadisticas_views.estadisticas_mesas, name='estadisticas_mesas'),
    path('estadisticas/productos/', estadisticas_views.estadisticas_productos, name='estadisticas_productos'),
    path('estadisticas/ventastotales/', estadisticas_views.ventas_totales, name='ventas_totales'),
    path('estadisticas/reportes/', estadisticas_views.reportes, name='reportes'),
    path('estadisticas/reporte_pdf/', estadisticas_views.reporte_pdf, name='reporte_pdf'),

    path('menus/', include('menu.urls')),
    path('convertir/', convertir_divisa, name='convertir_divisa'),
]
