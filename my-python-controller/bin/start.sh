#!/bin/bash

if [ -z ${CONFIG_FILE+x} ]; then
  python3.6 /opt/my-controller/${FILE_NAME} "INSIDE_POD"
else
  python3.6 /opt/my-controller/${FILE_NAME} --config ${CONFIG_FILE}
fi
