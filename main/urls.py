from django.contrib import admin
from django.urls import path, include
from sigin.views import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('profile/', include('profiles.urls')),
    path('appointments/', include('appointments.urls')),
    path('case/', include('case.urls')),
    path('reports/', include('reports.urls')),
    path('bill/', include('bill.urls')),
	path('login/', login),
    path('logout/', logout),
    path('login/', include('sigin.urls'))
]
