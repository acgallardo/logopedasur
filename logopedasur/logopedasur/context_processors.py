from django.conf import settings

def basedir(request):
    return {'BASE_DIR': settings.BASE_DIR}
