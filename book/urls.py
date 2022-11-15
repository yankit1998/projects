from django.urls import path
from book import views

urlpatterns = [
    path('add/',views.add),
    path('register/',views.register),
    path('login/',views.userlogin),
    path('delete/<int:tid>',views.delete),
    path('update/<str:tid>',views.update),
    path('refresh/',views.refersh),
    path('ltoh/',views.priceLtoH),
    path('htol/',views.priceHtoL),
    path('asc/',views.nameasc),
    path('dsc/',views.namedsc),
    path('reference/',views.reference),
    path('fiction/',views.fiction),
    path('nfiction/',views.nfiction),
    path('edited/',views.edited)

]
