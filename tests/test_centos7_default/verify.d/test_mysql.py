def test_mysql_process(host):
    assert host.service("my_db-mysql").is_running
    assert host.service("my_db-mysql").is_enabled

def test_check_mysql_access(host):
    assert host.run("mysql --protocol=tcp -h 127.0.0.1 -u u1 -P 13306 -ppassword1 db1").succeeded
    assert host.run("mysql --protocol=tcp -h 127.0.0.1 -u u1 -P 13306 -ppassword1 db2").failed
    assert host.run("mysql --protocol=tcp -h 127.0.0.1 -u u1 -P 13306 -ppassword2 db1").failed

    assert host.run("mysql --protocol=tcp -h 127.0.0.1 -u u3 -P 13306 -ppassword3 db1").succeeded
    assert host.run("mysql --protocol=tcp -h 127.0.0.1 -u u3 -P 13306 -ppassword3 db2").succeeded
    assert host.run("mysql --protocol=tcp -h 127.0.0.1 -u u3 -P 13306 -ppassword3 db3").failed
def test_backup_and_restore(host):
    assert host.run("echo 'select * from test_table | mysql --protocol=tcp -h 127.0.0.1 -u u1 -P 13306 -ppassword1 db1").failed
    host.run("echo 'drop table if exists test_table' | mysql --protocol=tcp -h 127.0.0.1 -u u1 -P 13306 -ppassword1 db1")
    host.run("echo 'create table test_table(first char(255), second integer)' | mysql --protocol=tcp -h 127.0.0.1 -u u1 -P 13306 -ppassword1 db1")
    host.run("""echo 'insert into test_table values("one",1)' | mysql --protocol=tcp -h 127.0.0.1 -u u1 -P 13306 -ppassword1 db1""")
    host.run("""echo 'insert into test_table values("two",2)' | mysql --protocol=tcp -h 127.0.0.1 -u u1 -P 13306 -ppassword1 db1""")

    backup_file = host.ansible(
      "command",
      "~/mysql/bin/backup.sh db1",
      become=True,
      become_user="my_db",
      check=False,
    )['stdout'].strip()
    host.run("""echo 'drop table test_table' | mysql --protocol=tcp -h 127.0.0.1 -u u1 -P 13306 -ppassword1 db1""")

    host.ansible(
      "command",
      "~/mysql/bin/restore.sh db1 ~/mysql/backups/{file}.sql".format(file=backup_file),
      become=True,
      become_user="my_db",
      check=False,
    )
    assert host.check_output("""echo 'select * from test_table where first="one"' | mysql -N --protocol=tcp -h 127.0.0.1 -u u1 -P 13306 -ppassword1 db1""").strip() == "one\t1"
    assert host.check_output("""echo 'select * from test_table where first="two"' | mysql -N --protocol=tcp -h 127.0.0.1 -u u1 -P 13306 -ppassword1 db1""").strip() == "two\t2"
