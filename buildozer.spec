[app]

# (str) Title of your application
title = FTSApp

# (str) Package name
package.name = ftsapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.fts

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv

# (list) List of inclusions using pattern matching
source.include_patterns = FreeTAKServer/*

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (str) Application versioning (method 2)
version = 2.5

# (list) Application requirements
requirements = python3,kivy==2.1.0,android,android.permissions,android.storage,kivymd,pillow,flask==2.0.3,werkzeug==2.0.3,flask-sqlalchemy==2.5.1,libxml2==2.9.10,libxslt==1.1.31,protobuf==3.20.3,docutils==0.18.1,more-itertools==8.12.0,flask_login,pyOpenSSL,flask_migrate,flask_wtf,email_validator,gunicorn,coveralls,coverage,pytest,flake8,flake8-print,pep8-naming,selenium,lxml,waitress,cheroot,python-socketio,flask_httpauth,scrapy,python-engineio,cryptography,wheel,pathlib,sqlalchemy,setuptools,jaraco.functools,bidict,jnius

# (str) Custom source folders for requirements
# Sets custom folder for the requirements
#requirements.source.kivy = ../../kivy
#requirements.source.android = ../../android

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Use the new python3 implementation to android instead of the old python2
#python_version = 3

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, FOREGROUND_SERVICE, POST_NOTIFICATIONS

# (int) Target Android API, should be as high
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (list) List of service to declare
services = myfts:./FreeTAKServer/controllers/services/FTS.py:foreground:sticky

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
