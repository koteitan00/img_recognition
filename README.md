# img_recognition

文字認識を用いて本棚の書籍位置を検知するシステム  
具体的には、webカメラから取得した画像にYOLO7での物体検知を適応した上で書籍の背表紙画像の切り出しを行う  
切り出した画像にOCRを使用し背表紙ラベルを取得することでリアルタイムに書籍の位置取得、検知を行うことができる


# DEMO

"hoge"の魅力が直感的に伝えわるデモ動画や図解を載せる

# Features

"hoge"のセールスポイントや差別化などを説明する

# Requirement
```
import io
import os
import os.path
import matplotlib.pyplot as plt
import cv2
import csv
import numpy as np
from PIL import Image
from io import BytesIO
from heic2png import HEIC2PNG
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload
```

# Installation

Requirementで列挙したライブラリなどのインストール方法の説明

# Usage

# Note

注意点などがあれば書く

# Author

* 星　海里
* 千葉工業大学先進工学部未来ロボティクス学科/千葉工業大学自律ロボット研究室
* hoshikairi00@gmail.com

# License

"img_recognition" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

"img_recognition" is Confidential.
