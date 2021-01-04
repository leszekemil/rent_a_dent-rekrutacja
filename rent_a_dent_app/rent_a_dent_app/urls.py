"""rent_a_dent_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rent_a_dent import views
from rent_a_dent.views import VisitsList, AddVisit, VisitDetails, VisitViewSerializer, VisitListViewSerializer, UpdateVisitView, DeleteVisitView

urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('visits/', views.VisitsList.as_view(), name='visits_list'),
    path('visit/add/', views.AddVisit.as_view(), name='visit_add'),
    path('visit/<int:visit_id>/', VisitDetails.as_view(), name='visit_details'),
    path('visit/update/<int:pk>/', UpdateVisitView.as_view(), name='visit_update'),
    path('visit/delete/<int:pk>/', DeleteVisitView.as_view(), name='visit_delete'),

    path('serialized/visit/', VisitListViewSerializer.as_view()),
    path('serialized/visit/<int:pk>/', VisitViewSerializer.as_view()),


]
