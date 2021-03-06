import os
import requests
import config
import zipfile
import shutil

def create_directory():
    if not os.path.exists(config.folder_name):
        os.makedirs(config.folder_name)

def download_image(url, name):
    r = requests.get(url)
    open(config.folder_name+"/"+name, 'wb').write(r.content)


def zip_dir():
    zip_name = config.zip_name
    print("Creating the zip of images:", zip_name)
    zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    folder_name = config.folder_name
    print("Zipping the files:")
    for root, dirs, files in os.walk(folder_name):
        print(root)
        for file in files:
            print(" -", file)
            zipf.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file), os.path.join(folder_name, '..'))
                       )
    zipf.close()

def delete_dir():
    shutil.rmtree(config.folder_name)

# Sample usage
# create_directory()
# download_image("https://mars.nasa.gov/msl-raw-images/msss/02688/mcam/2688ML0140720091002937C00_DXXX.jpg", "2688ML0140720091002937C00_DXXX.jpg")
# zipdir()
# delete_dir()