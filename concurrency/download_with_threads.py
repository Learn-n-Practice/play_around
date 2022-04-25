import requests
import concurrent.futures as cf
from time import  perf_counter

start = perf_counter()
urls =[
    'https://unsplash.com/photos/AnzxhCjE1v0',
    'https://unsplash.com/photos/NgpzA_Yqc4I',
    'https://unsplash.com/photos/2UsrIbuag6A',
    'https://unsplash.com/photos/9X7v20kF3BM',
    'https://unsplash.com/photos/I4Kjh7xTGS4',
    'https://unsplash.com/photos/KQw-jbHsNyA',
    'https://unsplash.com/photos/TPMMAIS-8fs',
    'https://unsplash.com/photos/Jt_Kco5hkvQ',
    'https://unsplash.com/photos/zmL1XMHsq3g',
    'https://unsplash.com/photos/PeDgQ7_na80',
    'https://unsplash.com/photos/ogKr6S5pSGE'
]

def download_image(url):
    print(f"Dowloading image from {url}...")
    image_bytes = requests.get(url)
    image_name = url.split('/')[3]
    image_name = f"{image_name}.jpg"
    with open(f'/images/{image_name}', 'wb') as img_f:
        img_f.write(image_bytes)
        print(f"Image {image_name} downloaded")


# Threads to download each image
with cf.ThreadPoolExecutor() as executor:
    downloads = executor.map(download_image, urls)


finish = perf_counter()
print(f"Done downloading images in {round(finish-start, 2)} seconds")