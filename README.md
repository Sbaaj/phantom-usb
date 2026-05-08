# phantom-usb

*A python-based filesystem watcher that unlocks a hidden **VeraCrypt** volume via a trigger file.*

phantom-usb is a lightweight Python script that monitors a directory for a trigger file. When detected, it reads the password from the file, immediately destroys it, and passes the password to VeraCrypt to mount a hidden encrypted volume on a USB drive. 

The purpose of **phantom-usb** is to turn any USB into a dead drop vault. A single VeraCrypt container on the drive holds two layers: 

1. An outer decoy volume with fake files and a decoy password
2. A hidden inner volume with your real data and a real password

## How it works

phantom-usb uses python's watchdog library to monitor a directory. When a file named "mountunlock.txt" is dropped into the watched directory, the script reads the password from it, immediately deletes the file, and then passes the password to VeraCrypt via CLI to silently mount the hidden volume. The password never touches your terminal history, and the trigger file exists for less than a second. 

## Use case

If the drive is ever seized you hand over the *decoy* password, they see nothing suspicious. Somewhere safe, dropping a trigger file with the *real* password into a watched directory silently mounts the hidden volume and immediately removes the trigger file.

