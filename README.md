# Dev Notes

## API Hits
Sources:

https://itch.io/t/1588368/download-a-game-with-the-api

https://github.com/itchio/itch.io/issues/992

- Can add .xml to get the RSS feed for a search url:
    - https://itch.io/games/free/tag-gameboy-advance
    - https://itch.io/games/free/tag-gameboy-advance.xml

- Search for a game
    - old style: https://itch.io/api/1/me/search/games?query=x-moon
    - newer style: https://api.itch.io/search/games?query=x-moon

- Get info based on game ID
    - https://api.itch.io/games/415790
    - This link should work for you in the browser, if you're logged in - for API usage, you'll need an API key (see User settings). You can pass it with the Authorization header. (Source: https://github.com/itchio/itch.io/issues/992)

- Get ID based on author and game name:
    - https://thorbjorn.itch.io/tiled/data.json

- get download link:
    - old: https://itch.io/api/1/{constants.API_KEY}/upload/504289/download
    - THIS DOES NOT WORK: https://api.itch.io/upload/504289/download