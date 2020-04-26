from django.shortcuts import render
from django.conf import settings
from .models import Camera
from math import ceil
import os

videos_path = settings.MEDIA_ROOT


def camerapage(request):
    return render(request=request,
                  template_name="cameras/watch.html",
                  context={"Cameras": Camera.objects.all()})


def watch(request, cam_name):
    for cam in Camera.objects.all():
        if cam.title == cam_name:
            return render(request=request,
                          template_name="cameras/watch.html",
                          context={"camera": cam, "cameras": Camera.objects.all()})
    return render(request=request,
                  template_name="home/unknown_page.html",
                  context={"cameras": Camera.objects.all()})


def replay(request,cam_name, page_number=1):
    try:
        page_number = int(page_number)
    except ValueError:
        return render(request=request,
                      template_name="home/unknown_page.html",
                      context={"cameras": Camera.objects.all()})

    class Video:
        def __init__(self, path, title):
            self.path = path
            self.title = title

        def __str__(self):
            return self.title

    class Date:
        videos = []

        def __init__(self, path, date):
            self.path = path
            self.date = date

        def __str__(self):
            return self.date

    for cam in Camera.objects.all():
        if cam.title == cam_name:
            dates = []

            for dir_or_file in os.listdir(os.path.join(videos_path, cam.path)):
                date_folder_path = os.path.join(os.path.join(videos_path, cam.path), dir_or_file)
                if os.path.isdir(date_folder_path):
                    new_date = Date(date_folder_path, dir_or_file)
                    for possible_file in os.listdir(date_folder_path):
                        if str(possible_file).endswith("MJPEG.mp4"):
                            continue
                        file_path = os.path.join(date_folder_path, possible_file)
                        if os.path.isfile(file_path):
                            new_video = Video(os.path.join(dir_or_file, possible_file), possible_file.replace("-", ":"))
                            new_date.videos.append(new_video)
                    dates.append(new_date)

            dates.sort(key=lambda x: x.date, reverse=True)
            for date in dates:
                date.videos.sort(key=lambda x: x.title, reverse=True)

            page_amount = ceil(len(dates)/7)
            begin = 0 + (page_number-1)*7
            end = 7 + (page_number-1)*7
            begin_end = "{}:{}".format(begin, end)

            return render(request=request,
                          template_name="cameras/replay.html",
                          context={"dates": dates, "page_amount": page_amount, "current_page": page_number,
                                   "begin_end": begin_end, "cameras": Camera.objects.all(), "camera": cam})

    return render(request=request,
                  template_name="home/unknown_page.html",
                  context={"cameras": Camera.objects.all()})
