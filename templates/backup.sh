#!/bin/bash
DATABASE=$1
DATE=$(date +"%Y-%m-%d_%H%M%S")
if [ -z "$DATABASE" ]; then
    echo "usage: $0 <database>"
    exit 1
fi

FILENAME=${DATABASE}_${DATE}
mkdir -p {{ app.value.mysql.user.home }}/mysql/backups
mysqldump -u {{ app.value.mysql.user.user }} -S {{ app.value.mysql.user.home }}/mysql/var/mysql.sock $DATABASE > {{ app.value.mysql.user.home }}/mysql/backups/${FILENAME}.sql
echo $FILENAME
