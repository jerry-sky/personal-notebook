#!/bin/bash

# get current timestamp
cur_time=$(date +%Y-%m-%d_%H-%M-%S)

# keep the original file just in case
sudo cp /etc/fstab /etc/fstab.$cur_time.original

list="$(sudo blkid)\n"
# choose the drive
printf "$list" | grep ^ -n

drive_count=$(printf "$list" | wc -l)

# prompt the user for the drive they want to automount
read id

id="${id//[!0-9]*/}"

if [ -z "$id" ]; then
    echo 'provide a number'
    exit 1
fi

if [ "$id" -lt 1 -o "$id" -gt "$drive_count" ]; then
    echo 'provide a natural number between 1 and '$drive_count
    exit 1
fi

chosen=$(printf "$list" | head -n$id | tail -n1 )
# extract the UUID
# strip the ‘front’: ~~'/dev/sda: UUID="'~~
uuid="${chosen/* UUID\=\"/}"
# strip the ‘back’: ~~'" whatever'~~
uuid="${uuid/\"*}"

# extract the partition type
# strip the ‘front’: ~~'/dev/sda: … TYPE="'~~
type="${chosen/* TYPE\=\"/}"
# strip the ‘back’: ~~'" whatever'~~
type="${type/\"*}"

# create the target mount directory
read -p "Provide the name of the directory that will be created in /media/"$USER": " dir
dir="/media/$USER/$dir"
sudo mkdir -p "$dir"

# append the entry to `/etc/fstab`
printf "UUID=$uuid $dir $type defaults,uid=1000,gid=1000,umask=022,rw 0 2\n" | sudo tee -a /etc/fstab >/dev/null
