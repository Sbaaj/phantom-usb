# phantom-usb

*A python-based filesystem watcher that unlocks a hidden **veracrypt** volume via a trigger file.*

The purpose of **phantom-usb** is to turn any USB into a sleeper agent. A single veracrypt container on the drive  holds two layers: 

1. An outer decoy volume with fake filers and a decoy password
2. A hidden inner volume with your real data and a real password

If the driver is ever seized you hand over the *decoy* password, they see nothing suspicous. Somewhere safe, dropping a trigger file with the *real* password into a watched directory silently mounts the hidden volume and immediately removes the trigger file.

