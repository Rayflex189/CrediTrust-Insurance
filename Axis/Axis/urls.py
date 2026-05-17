"""
URL configuration for Axis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.management import call_command
from django.conf.urls.static import static
from django.conf import settings

# Temporary view to run migrations (REMOVE AFTER USING!)
@csrf_exempt
def run_migrations(request):
    if request.method == 'POST':
        try:
            call_command('migrate', interactive=False)
            return JsonResponse({'status': 'success', 'message': 'Migrations completed successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'POST request required'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('axis_app.urls')),
    path('run-migrations/', run_migrations),  # TEMPORARY - remove this after migrations are done
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
