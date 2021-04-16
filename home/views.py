from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render, redirect
from cameras.models import Camera
from django.conf import settings
import os


def get_recordings():

    class Video:
        path = ''
        title = ''

        def __init__(self,path,title):
            self.path = path
            self.title = title

        def __str__(self):
            return self.title

    videos = []

    for camera_folder in os.listdir(settings.MEDIA_ROOT):
        if os.path.isdir(os.path.join(settings.MEDIA_ROOT, camera_folder)):
            for dir_or_file in os.listdir(os.path.join(settings.MEDIA_ROOT, camera_folder)):
                date_folder_path = os.path.join(os.path.join(settings.MEDIA_ROOT, camera_folder), dir_or_file)
                if os.path.isdir(date_folder_path):
                    for possible_file in os.listdir(date_folder_path):
                        if str(possible_file).endswith("MJPEG.mp4"):
                            continue
                        file_path = os.path.join(date_folder_path,possible_file)
                        if os.path.isfile(file_path):
                            new_video = Video(os.path.join(camera_folder, dir_or_file, possible_file),
                                              date_folder_path.split("/")[-1].split("\\")[-1]+" "+possible_file.replace("-",":"))
                            videos.append(new_video)
                if os.path.isfile(date_folder_path):
                    filepath = date_folder_path
                    if str(filepath).endswith("MJPEG.mp4"):
                            continue
                    new_video = Video(os.path.join(camera_folder, dir_or_file),
                                        filepath.split("/")[-1].split("\\")[-1])
                    videos.append(new_video)

    videos.sort(key=lambda x: x.title, reverse=True)

    return videos[0:10]


def index(request):
    cameras = Camera.objects.all()
    return render(request=request,
                  template_name="home/index.html",
                  context={"recordings": get_recordings(), "cameras": cameras})


def logout_request(request):
    logout(request)
    return redirect("/")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    form = AuthenticationForm()
    if request.user.is_authenticated:
        return redirect("/")
    else:
        return render(request, "base/login.html", context={"form": form, "template": "base/base.html"})
