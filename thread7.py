import time
import concurrent.futures
import requests
img_urls = [
    "https://media.istockphoto.com/id/1272468011/fr/photo/joueur-de-tennis-f%C3%A9minin-professionnel-servant-la-bille-pendant-le-\
match.jpg?s=612x612&w=0&k=20&c=6ugPl_1W8Ye-aErWj2sXoFDUwtrRhtTSf2RQZ_w81to=",
    "https://media.istockphoto.com/id/941529542/fr/photo/\
joueuse-de-tennis-concept-sport-de-loisirs.jpg?s=612x612&w=0&k=20&c=yENnB3sb55n_SnMSLzhoVJ4OsqHfGY2ZnJB8PTzY-hg="
]
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4] + '.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")
#for img_url in img_urls:
# download_images(img_url)