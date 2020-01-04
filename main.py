import pymysql.cursors


def db_connect(db='db'):
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='somestrongpassword',
                                 db=db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection


def create_database():
    connection = db_connect(None)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "CREATE DATABASE IF NOT EXISTS db"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()


def create_users_table():
    connection = db_connect()
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "CREATE TABLE IF NOT EXISTS `users` (`id` int(11) NOT NULL AUTO_INCREMENT, `email` varchar(255) COLLATE utf8_bin NOT NULL, `password` varchar(255) COLLATE utf8_bin NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1;"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()


def init_db():
    create_database()
    create_users_table()


def do_something():
    init_db()

    connection = db_connect()
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()


if __name__ == "__main__":
    do_something()
