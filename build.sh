#!/usr/bin/env bash

make install && psql -a -d $DATABASE_URL -f python-project-52/db.sqlite3
