import urllib.request
import os
import ssl
from tqdm import tqdm

def download_with_progress(url, local_path):
    ssl_context = ssl._create_unverified_context()

    with urllib.request.urlopen(url, context=ssl_context) as response, open(local_path, 'wb') as output_file:
        file_size = int(response.headers['Content-Length'])
        block_size = 1024

        with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
            while True:
                data = response.read(block_size)
                if not data:
                    break
                output_file.write(data)
                pbar.update(len(data))

url = (
    "https://api.worldbank.org/v2/en/indicator/"
    "NY.GDP.MKTP.CD?downloadformat=csv"
)
local_path = "gdp_by_country.zip"

download_with_progress(url, local_path)



