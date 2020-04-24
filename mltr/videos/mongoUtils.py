from pymongo import MongoClient
import pymongo
from sshtunnel import open_tunnel
from sshtunnel import SSHTunnelForwarder, create_logger
import os
from django.conf import settings
from bson import json_util
from bson.objectid import ObjectId
import json
import gridfs
from .models import Video
from django.utils.dateparse import parse_datetime


class MongoUtils:
    host = "ec2-18-188-66-52.us-east-2.compute.amazonaws.com"
    ssh_username = "ubuntu"
    ssh_private_key = os.path.join(settings.BASE_DIR,"ML_test.pem")
    def __init__(self):
        self.server = SSHTunnelForwarder(
            (self.host, 22),
            ssh_username = self.ssh_username,
            ssh_private_key = self.ssh_private_key,
            remote_bind_address=('127.0.0.1', 27017)
        )
    
    def resource_handler(func):
            def handle_connection(*args):
                _self = args[0]
                try:
                    print("Connecting to database...")
                    _self.server.daemon_forward_servers = True
                    _self.server.start()
                    _self.client = MongoClient('127.0.0.1', _self.server.local_bind_port)
                    _self.db = _self.client['bdr_db']
                    res = func(*args)
                    return res
                except Exception as e:
                    print("Exception occurs: ", e)
                finally:
                    _self.server.stop()
                    print("Connection closed")
            return handle_connection

    @resource_handler
    def find_videos_by_phone(self, phone):
        reports = self.db.baddriverreports
        videos = self.db['fs.files']
        res = []
        for report in reports.find({"postingAccount": phone}).sort('time', pymongo.DESCENDING):
            video_info = {"id": report['videoClip'], "user": report['reporterName'], 'license_plate': report['licensePlateNumber'], 'created': report['time']}
            video = videos.find_one({'_id': report['videoClip']})
            # Once the backend is modified, speed data will be available in database, you should use the following code
            # video_info["init_speed"] = video['metadata']['initialSpeed']
            # video_info["avg_speed"] = video['metadata']['averageSpeed']
            # video_info["final_speed"] = video['metadata']['finalSpeed']
            video_info["location"] = video['metadata']['locationRecorded']
            # print(video_info)
            video_info = json.loads(json_util.dumps(video_info))
            res.append(video_info)
        print(len(res))
        return res
    
    @resource_handler
    def get_video_by_id(self, id, filename):
        print("try to get video")
        fs = gridfs.GridFSBucket(self.db)
        preview_file_path = os.path.join(settings.MEDIA_ROOT, filename)
        file = open(preview_file_path, 'wb+')
        fs.download_to_stream(ObjectId(id), file)

    def convert_to_video_model(self, video_info):
        video = Video()
        video.title = video_info['title']
        video.description = video_info['description']
        video.created = parse_datetime(video_info['created'])
        video.location = video_info['location']
        video.license_plate = video_info['license_plate']
        self.get_video_by_id(str(video_info['id']['$oid']), "videos/" + video_info['title'] + ".mp4")
        video.video.name = "videos/" + video_info['title'] + ".mp4"
        video.save()
        


        





