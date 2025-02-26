from django.contrib import admin
from django.urls import path, include

# Import debug_toolbar correctly
import debug_toolbar  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),  # Debug Toolbar URL
    path('', include('events.urls')),  # Include your app URLs
]
