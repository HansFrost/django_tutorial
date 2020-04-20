#!/bin/bash

echo "Running command '$*'"

exec /bin/bash -c "$*"


# Denne kommando virker: exec $*

#original script kommando: exec su -p - ${PYTHON_RUN_USER} -s /bin/bash -c "$*"