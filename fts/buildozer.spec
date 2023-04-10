[app]

# (str) Title of your application
title = FTS2App

# (str) Package name
package.name = fts2app

# (str) Package domain (needed for android/ios packaging)
package.domain = org.fts

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv

# (list) List of inclusions using pattern matching
#source.include_patterns = FreeTAKServer/*

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
version = 1.3

# (list) Application requirements
requirements = hostpython3==3.8.16,python3==3.8.16,kivy==2.1.0,android,android.permissions,android.storage,kivymd,pillow,Flask==2.0.3,certifi==2022.12.7,charset-normalizer==3.1.0,idna==3.4,urllib3==1.26.15,requests==2.28.2,Werkzeug==2.0.3,Flask-SQLAlchemy==2.5.1,libxml2==2.9.10,libxslt==1.1.31,SQLAlchemy==1.4.47,lxml,protobuf==3.20.3,docutils==0.18.1,more-itertools==8.12.0,click==8.0.4,colorama==0.4.4,defusedxml==0.7.1,dnspython==2.2.1,eventlet==0.33.3,Flask-Cors==3.0.9,Flask-SocketIO==4.3.1,geographiclib==1.52,geopy==2.2.0,greenlet==2.0.2,itsdangerous==2.0.1,pbr==5.11.1,testresources==2.0.1,Jinja2==3.1.2,MarkupSafe==2.0.1,monotonic==1.6,pathlib2==2.3.7.post1,psutil==5.9.4,pykml==0.2.0,PyYAML==6.0,six==1.16.0,tabulate==0.8.7,WTForms==2.3.3,qrcode==7.3.1,Flask-Login,pyOpenSSL,Flask-Migrate,Flask-WTF,email_validator,gunicorn,coveralls,coverage,pytest,flake8,flake8-print,pep8-naming,selenium,waitress,cheroot,python-socketio,Flask-HTTPAuth,scrapy,python-engineio,cryptography,wheel,setuptools,jaraco.functools,bidict,xmltodict,jnius

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
services = Myfts:my_service.py:foreground

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
