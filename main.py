import streamlit as st
import os

st.header("Spotify Playlist Downloader")
input = st.text_input("Paste the Link here")

if os.path.exists("files") == False:
  os.mkdir("files")

if input:
  start = st.button("Start Extracting the Audio files")
  if start:
    downloading = os.system(f"spotdl {input}")
    for filename in os.listdir():
      os.system(f"cp {filename} files")
    os.system("zip -r hosanna_songs.zip files")
    start = False
  if start == False:
    st.download_button("Download Now","hosanna_songs.zip")
