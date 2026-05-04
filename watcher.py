# Watches directory for a trigger file, then mounts a veracrypt hidden volume
<<<<<<< HEAD

=======
>>>>>>> e4789e676c894225833171d3804b18b2305ac554
import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            if filename == "mountunlock.txt": 

<<<<<<< HEAD
                try:
                    with open(event.src_path, 'r') as file:
                        password = file.read().strip()

                        if not password:
                            return
                
                        print("Password found:", password)

                        time.sleep(0.1)
                        os.remove(event.src_path)
                
                except Exception as e:
                    print("Couldn't read file:", e) 

=======
>>>>>>> e4789e676c894225833171d3804b18b2305ac554
path = os.path.dirname(os.path.abspath(__file__))

observer = Observer()
observer.schedule(Handler(), path)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
