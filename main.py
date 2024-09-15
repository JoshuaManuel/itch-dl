import requests

def download_file(url: str, filename: str):
    # Send a GET request to the URL
    r = requests.get(url, stream=True)
    print(r.status_code)

    # Check if the request was successful
    if r.status_code == 200:
        print("request successful")
        # Open the file in write mode
        with open(filename, 'wb') as f:
            # Write the content of the response to the file
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def main():
    upload_id = "5437329"
    api_key = "" # insert API key
    url = "https://itch.io/uploads/{upload_id}/download?api_key={api_key}"

    print("Downloading game.zip...")
    download_file(url, "game.zip")
    print("Download complete!")


if __name__ == "__main__":
    main()