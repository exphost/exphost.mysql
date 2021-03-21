#!/bin/bash
DATABASE=$1
FILENAME=$2
if [ -z "$DATABASE" ]; then
    echo "missing database"
    echo "usage: $0 <database> <filename>"
    exit 1
fi

if [ -z "$FILENAME" ]; then
    echo "missing filename"
    echo "usage: $0 <database> <filename>"
    exit 2
fi

if [ ! -e $FILENAME ]; then
    echo "backup file does not exists"
    echo "usage: $0 <database> <filename>"
    exit 3
fi

mysql -u {{ app.value.mysql.user.user }} -h {{ inventory_hostname }} -p{{ app.value.mysql.configs.pass }} -P {{ app.value.mysql.configs.port }} $DATABASE < ${FILENAME}
