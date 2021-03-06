import logging
from redis import Redis
import config
import image_storage_handler

r= Redis(
    host=config.host,
    port=config.port,
    db=config.db
)

#Download the images in  folder
if __name__ == '__main__':
    image_storage_handler.create_directory()
    print("Created images folder")
    result = ""
    while result != config.end_marker:
        print("Waiting for a new item:")
        result = r.blpop(config.queue_name)[1].decode('utf-8')
        if result != config.end_marker:
            file_name = result.split('/')[-1]
            image_storage_handler.download_image(result, file_name)
            print("Fetched and stored the image: ", file_name)
        else:
            print("Received end marker, exiting!")
    print("Creating image bundle: ", config.zip_name)
    image_storage_handler.zip_dir()
    image_storage_handler.delete_dir()
