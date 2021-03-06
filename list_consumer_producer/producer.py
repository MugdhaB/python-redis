import logging
from redis import Redis
from mars_photo_retriever import get_mars_photo
from dates_in_month import get_dates
import config

r= Redis(
    host=config.host,
    port=config.port,
    db=config.db
)

if __name__ == '__main__':
    for date in get_dates(2, 2020):
        url = get_mars_photo(date)
        print("Pushing the photo : ", url.split('/')[-1])
        r.lpush(config.queue_name, url)
    print("Pushing the end marker!")
    r.lpush(config.queue_name, config.end_marker)