from django.shortcuts import render
from django.views import generic
from .models import Course, Video
from django.shortcuts import get_object_or_404

# from .forms import CourseForm

# Create your views here.

class CourseListView(generic.ListView):
    template_name = "content/course_list.html"
    queryset = Course.objects.all()
    
class CourseDetailView(generic.DetailView):
    template_name = "content/course_detail.html"
    queryset = Course.objects.all()
    
class VideoDetailView(generic.DetailView):
    template_name = "content/video_detail.html"

    def get_object(self):
        video = get_object_or_404(Video, slug=self.kwargs["video_slug"])
        return video
        
    def get_queryset(self):
        course = get_object_or_404(Course, slug=self.kwargs["slug"])
        return Course.video.all()