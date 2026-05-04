# Watches directory for a trigger file, then mounts a veracrypt hidden volume

import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print("File Detected:", event.src_path) 

path = sys.argv[1]

observer = Observer()
observer.schedule(Handler(), path)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()