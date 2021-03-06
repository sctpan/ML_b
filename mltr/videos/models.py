from django.db import models
from django.urls import reverse
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=50, blank=True, default=None)
    description = models.CharField(max_length=500, blank=True, null=True, default=None)
    video = models.FileField(upload_to='videos/', null=True, blank=False, default=None)
    # thumbnail = models.ImageField(upload_to='images', default='default.jpg')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    ### add
    location = models.CharField(max_length=30, blank=True, null=True, default=None)
    license_plate = models.CharField(max_length=20, blank=True, null=True, default=None)
    avg_speed = models.CharField(max_length=10, blank=True, null=True, default=None)
    c_top = models.IntegerField(blank=True, null=True, default=None)
    c_left = models.IntegerField(blank=True, null=True, default=None)
    c_bot = models.IntegerField(blank=True, null=True, default=None)
    c_right = models.IntegerField(blank=True, null=True, default=None)
    c_frame = models.IntegerField(blank=True, null=True, default=None)

    def get_absolute_url(self):
        return reverse("video_detail", kwargs={"video_id": self.id}) #f"/videos/{self.id}"