import streamlit as st
import os

st.header("Spotify Playlist Downloader")
input = st.text_input("Paste the Link here")

if os.exists("files") == False:
  os.mkdir("files")

if input == True:
  start = st.button("Start Extracting the Audio files")
  if start == True:
    downloading = os.system(f"spotdl {input}")
    for filename in os.listdir():
      os.system(f"cp {filename} files")
    os.system("zip -r hosanna_songs.zip files")
    start = False
  st.download_button("Download Now","hosanna_songs.zip")
