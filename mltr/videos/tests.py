from django.test import TestCase
from pymongo import MongoClient
from sshtunnel import open_tunnel
from sshtunnel import SSHTunnelForwarder
from .mongoUtils import MongoUtils

def test():
    mongoUtils = MongoUtils()
    mongoUtils.find_videos_by_phone("13102617363")

        

   


