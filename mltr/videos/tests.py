from django.test import TestCase
from pymongo import MongoClient
from sshtunnel import open_tunnel
from sshtunnel import SSHTunnelForwarder
from .mongoUtils import MongoUtils

def test():
    mongoUtils = MongoUtils()
    # mongoUtils.find_videos_by_phone("13102617363")
    
    mongoUtils.get_video_by_id("5e9cc84e5f487e13c6150f17")
    
    

        

   


