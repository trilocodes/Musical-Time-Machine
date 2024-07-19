# Musical-Time-Machine

This Python project fetches the top 100 songs for a given date from the Billboard Hot 100 chart and creates a Spotify playlist with those songs. Input a date, and the program handles the rest, from retrieving song details to adding them to your Spotify account.

### Features
- Fetches Billboard Hot 100 data for any given date
- Creates a Spotify playlist with the top 100 songs
- Outputs song titles, artists, and ranks
- Easy-to-use command-line interface

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/top-100-songs-to-spotify-playlist.git
   ```
2. Navigate to the project directory:
   ```bash
   cd top-100-songs-to-spotify-playlist
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your Spotify API credentials by creating a `.env` file in the project directory and adding the following:
   ```env
   SPOTIPY_CLIENT_ID='your_spotify_client_id'
   SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'
   SPOTIPY_REDIRECT_URI='your_spotify_redirect_uri'
   ```

### Usage
1. Run the script and input the desired date:
   ```bash
   python top_100_songs_to_spotify.py
   ```
2. Follow the prompts to log in to your Spotify account and enter the date (format: YYYY-MM-DD).

### Example
```bash
$ python top_100_songs_to_spotify.py
Enter a date (YYYY-MM-DD): 2020-07-19
Fetching top 100 songs for 2020-07-19...
Creating Spotify playlist...
Playlist created successfully! Check your Spotify account for "Top 100 Songs - 2020-07-19".
```
