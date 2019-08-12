#!/bin/bash

if [ -z ${CONFIG_FILE+x} ]; then
  python /opt/my-controller/watch.py
else
  python /opt/my-controller/watch.py --config ${CONFIG_FILE}
fi
