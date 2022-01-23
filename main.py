import time
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


CLIENT_ID = You client id
CLIENT_SECRET = your client secret
REDIRECT_URI='https://google.com'
USER_ID = your user id


s = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    show_dialog=True,
    scope='playlist-read-private playlist-read-private',
    cache_path='token.txt'))


playlists = s.current_user_playlists()['items']
melodic_techno_playlist = {}
melodic_techno_playlist_id = ""


for playlist in playlists:
    if 'MELODIC TECHNO 2022' in playlist['name']:
        melodic_techno_playlist_id = playlist['id']

result = s.playlist_items(melodic_techno_playlist_id, additional_types=['track'], limit=100)
all_tracks = []

while result:
    all_tracks.extend(result['items'])
    result = s.next(result)



for n in range(len(all_tracks)):
    melodic_techno_playlist[all_tracks[n]['track']['name']] = f"{all_tracks[n]['track']['artists'][0]['name']} "


track_name =[f"{i} {j}" for (i,j) in melodic_techno_playlist.items()]





# service = Service('/Users/ramiyammine/Developement/chromedriver')
#
# d = webdriver.Chrome(service=service)
# wait = WebDriverWait(d, 10)
# #
#
# for i in track_name:
#     print(i)
#     print('')
#     d.get('https://myfreemp3juices.cc/')
#     query = d.find_element(By.ID,'query')
#     query.click()
#     query.send_keys(i)
#     query.send_keys(Keys.ENTER)
#     time.sleep(5)
#
#     all_lines = d.find_elements(By.CLASS_NAME,'list-group')
#     for line in all_lines:
#         original_window = d.current_window_handle
#         download_button_from_main_page = d.find_element(By.XPATH, '//*[@id="result"]/div[2]/li[1]/div/a[3]')
#         download_button_from_main_page.click()
#
#         for window_handle in d.window_handles:
#             if window_handle != original_window:
#                 d.switch_to.window(window_handle)
#                 time.sleep(10)
#                 DOWNLOAD_BUTTON = d.find_element(By.XPATH,'//*[@id="footer"]/div/div[1]/button')
#                 DOWNLOAD_BUTTON.click()
#                 time.sleep(3)
#                 break
#             elif window_handle != original_window:
#                 d.switch_to_window(window_handle)
#
#                 time.sleep(3)
#         time.sleep(5)

