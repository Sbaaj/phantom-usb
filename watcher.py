# Watches directory for a trigger file, then mounts a veracrypt hidden volume

import subprocess
import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

if len(sys.argv) < 3: 
    print("Usage: sudo python watcher.py <watch_path> <container_path>")
    sys.exit(1)

watch_path = sys.argv[1]
container_path = sys.argv[2]

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            if filename == "mountunlock.txt": 

                try:
                    with open(event.src_path, 'r') as file:
                        password = file.read().rstrip('\n')

                        if not password:
                            return

                        time.sleep(0.1)
                        os.remove(event.src_path)
                        print("Trigger file destroyed. mounting...")
                
                    subprocess.run([
                        "sudo", "veracrypt", "--text", "--mount",
                        container_path,
                        "/mnt",
                        f"--password={password}",
                        "--non-interactive"
                    ])
                    print("Volume mounted at /mnt")


                except Exception as e:
                    print("Couldn't read file:", e) 

observer = Observer()
observer.schedule(Handler(), watch_path)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()