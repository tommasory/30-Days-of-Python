import os
import requests
import shutil
from download_util import download_file
THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOADS_DIR, '1.jpg')
url = "https://cloudfront-us-east-1.images.arcpublishing.com/semana/OVY64Q5DURBOXMXRAB7SXUXRD4.jpg"

# a smallish item
r = requests.get(url, stream=True)
r.raise_for_status() # 200
with open(downloaded_img_path, 'wb') as f:
    f.write(r.content)

# Extraer elemnto basico del nombre
# dl_filename = os.path.basename(url)
# print(dl_filename)
# new_dl_path = os.path.join(DOWNLOADS_DIR, dl_filename)
# with requests.get(url, stream=True) as r:
#     with open(new_dl_path, 'wb') as file_obj:
#         shutil.copyfileobj(r.raw, file_obj)


download_file(url, DOWNLOADS_DIR)