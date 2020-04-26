# Django Camera view and playback

Project status: Finished.

A Django site to look at cameras(https://github.com/Ruud14/SecurityCamera) and watch replays.

# How to use:
- Clone this repository.
- run `pip install -r requirements.txt`.
- run `python manage.py migrate`.
- create a superuser by running `python manage.py createsuperuser`.
- run the server by running `python manage.py runserver`.
- login on `http://127.0.0.1:8000/login/`.
- go to `http://127.0.0.1:8000/admin/cameras/camera/` and press `add camera` in the top right corner of the screen.
- fill in the form with a title (E.g. `Camera1`), the url of your camera (E.g. `http://192.168.0.11:8000/stream.mjpg`) and the name of the folder that the recordings for this camera are in (E.g. `camera1`).
- Hit save and repeat the above 2 steps for every camera you want to add.
- Now in `settings.py` change the value of `MEDIA_ROOT` to the path of the parent directory of folder that the recordings for this camera are in (So here that would be the parent directory of `camera1` from the step before the previous step. E.g. `D:/camerastest/`).
- Now rerun the server and the site should be up and running `http://127.0.0.1:8000/`.

![index](https://github.com/Ruud14/Django-Camera-View-And-Playback/blob/master/pictures/index.jpg)
![index2](https://github.com/Ruud14/Django-Camera-View-And-Playback/blob/master/pictures/index2.jpg)
![replay](https://github.com/Ruud14/Django-Camera-View-And-Playback/blob/master/pictures/replay.jpg)
![watch](https://github.com/Ruud14/Django-Camera-View-And-Playback/blob/master/pictures/watch.jpg)
![replay_vid](https://github.com/Ruud14/Django-Camera-View-And-Playback/blob/master/pictures/replay_vid.jpg)

