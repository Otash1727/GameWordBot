from django.core.exceptions import ObjectDoesNotExist
from wordgame.models import MatchList,GamersList,ChempionsList
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()



def check_users(callback):
    checking=GamersList.objects.filter(user_id=callback)
    return checking