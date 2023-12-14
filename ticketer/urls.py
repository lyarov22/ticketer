from django.urls import include, path
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from userSystem import views as user_views

app_name = 'mySite'

urlpatterns = [
    path('favicon.ico/', RedirectView.as_view(url='/static/img/reread-logo.ico', permanent=True), name='favicon'),
    path('admin/', admin.site.urls),
    path('', include('mySite.urls')),


    # login system
    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),

    # profile system
    path('profile/', user_views.view_profile, name='view_profile'),
    path('profile/edit/', user_views.edit_profile, name='edit_profile'),

    path('profile/<str:username>/', user_views.other_user_profile, name='other_user_profile'),

    path('', include('benches.urls')),

    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),

    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
