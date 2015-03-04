#!/bin/bash --login

VIRTUAL_ENV_DIR=.venv
VIRTUAL_ENV_ACTIVATE=${VIRTUAL_ENV_DIR}/bin/activate
if [[ -e "${VIRTUAL_ENV_ACTIVATE}" ]]; then
    source "${VIRTUAL_ENV_ACTIVATE}"
else
    virtualenv-3.4 "${VIRTUAL_ENV_DIR}"
    source "${VIRTUAL_ENV_ACTIVATE}"
fi

pip3 install -r requirements.txt

export PYTHONPATH="/usr/local/lib/python3.4/dist-packages:$(pwd)"
echo "Received command line arguments: $#"

args=""
while [[ $# > 0 ]]; do
  switch="$1"

  case $switch in
    --python-file)
      source_file="$2"
      shift
      ;;
    *)
      args="$args $1"
    ;;
  esac

  shift
done

cmd="python3 $source_file $args"
echo "Executing ${cmd}"
exec $cmd
