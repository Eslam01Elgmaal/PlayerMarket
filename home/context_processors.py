from .models import Home


def home_data(request):
    return {
        "home": Home.objects.first()
    }