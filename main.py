import requests
import json
import constants
import utils

headers = {
    'Authorization': constants.API_KEY
}

def search_game(query: str):
    pass

def request_json(url: str):
    request = requests.get(url, headers=headers)
    obj = json.loads(request.content)
    print(obj)
    return request, obj

    #return json.loads(requests.get(url, headers=headers).content)


def download_game(upload_id: str, filename: str = None):
    # Get download link
    dl_url = request_json(f"https://itch.io/api/1/{constants.API_KEY}/upload/504289/download")

    if not filename:
        #filename = request_json(f"https://api.itch.io/games/{upload_id}")
        #filename = request_json(f"https://itch.io/api/1/{constants.API_KEY}/games/{upload_id}")
        _, game_info = request_json(f"https://api.itch.io/games/{upload_id}")
        filename = game_info["game"]["title"]
        filename = utils.slugify(filename)
        print(filename)

    #download_file(dl_url, utils.slugify(filename))

def get_game_id(game_id: str):
    pass

def download_file(url: str, filename: str):
    # Send a GET request to the URL
    r = requests.get(url, stream=True)
    
    # Check if the request was successful
    if r.status_code == 200:
        # Open the file in write mode
        with open(filename, 'wb') as f:
            # Write the content of the response to the file
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def main():
    pass

if __name__ == "__main__":
    download_game("11393136")
    #main()