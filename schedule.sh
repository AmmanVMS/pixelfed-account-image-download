#!/bin/bash
#
# regular retrival of images
#
# config

dst="/data/share/phone/picture-frame/"
server="https://pix.toot.wales"
user="ammanvms"
secret="secret.txt"
fromdate="2000-01-01"

# constants
log="$0.log"

( (
    date
    cd "`dirname \"$0\"`"

    source "ENV/bin/activate"

    if ! [ -d "$dst" ]; then
      echo "$dst does not exist"
      exit
    fi

    python3 ./download.py "$dst" "$server" "$user" "$secret" "$fromdate"
  )
  echo "Exit status $?"

) 2>&1 | tee "$log"
