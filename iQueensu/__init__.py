import sys

if sys.version_info.major > 2:
    import pymysql

    pymysql.install_as_MySQLdb()

