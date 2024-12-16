from vimeo_downloader import Vimeo
import sys

url = sys.argv[1]

v = Vimeo(url)
s = v.streams

best_stream = s[-1]

meta = v.metadata
title = meta.title

best_stream.download(download_directory='SurfVidz', filename=title+".mp4")
