import requests


mal_id = [36882, 49470, 51495]

for i in range(len(mal_id)):
    url = f"https://api.jikan.moe/v4/anime/{mal_id[i]}/full"
    r = requests.get(url).json()

    print(r["data"]["images"]["jpg"]["image_url"])

