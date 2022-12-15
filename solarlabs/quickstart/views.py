from django.shortcuts import render


import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bs4 import BeautifulSoup

# Create your views here.
@api_view(['GET'])
def get_natDetails(request,country_name):
    

    return Response({"flag_link":flag_link,"capitals":capitals,"largest_city":large_cities,"offical_languages":offical_languages,"area_total":area_total,"population":population,"GDP_nominal":GDP_nominal})
