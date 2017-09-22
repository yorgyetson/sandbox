#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A geek_beacon.taskapp beat -l INFO
