#!/usr/bin/env bash

make install && psql -a -d $DATABASE_URL -f postgres:///python-project-52