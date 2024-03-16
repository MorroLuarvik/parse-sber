from modules import downloader
import os

DIR_PATH = os.path.dirname(__file__)
DOWNLOAD_FOLDER = 'download'

download_path = os.path.join(DIR_PATH, DOWNLOAD_FOLDER)

url = "https://www.sberbank.ru/proxy/services/rates/public/v2/history?rateType=PMR-3&isoCode=A98&date=1705611600000&regionId=070"


downloader.load_files(url, download_path)
