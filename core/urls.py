from django_distill import distill_path
from .views import home


def get_home():
    return None  # No URL parameters needed for a simple index page

urlpatterns = [
    distill_path('', home, name='home', distill_func=get_home),
]