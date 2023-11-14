
from django.urls import path
from cafe import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("chefs", views.chefs, name="chefs"),
    path("menu", views.menu, name="menu"),
    path("offers", views.offers, name="offers"),
    path("staff", views.staff, name="staff"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path("reservation", views.reservation, name="reservation"),
    path("employees-form", views.employees, name="employees"),
    path("foods-form", views.foods, name="foods"),
    path("offers-form", views.offerform, name="offerform"),
    path('employees/delete/<int:emp_id>', views.employee_delete, name="delete_chef"),
    path('employees/update/<int:emp_id>', views.employee_update, name="update_chef"),
    path('offers/delete/<int:emp_id>', views.offers_delete, name="delete_offer"),
    path('offers/update/<int:emp_id>', views.offers_update, name="update_offer"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)