import pymysql

class Mysql:
    
    def __init__(self, host, user, password, db):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        self.cursor = self.connection.cursor()

    def select(self, sql, OnlyOne=False):
        response = { 'status': True, 'message': None}
        if not OnlyOne:
            try:
                self.cursor.execute(sql)
                data = self.cursor.fetchall()
                response['message'] = data
                return response
            except Exception as e:
                response = { 'status': False, 'message': e}
                return response
        else:
            try:
                self.cursor.execute(sql)
                data = self.cursor.fetchone()
                response['message'] = data
                return response
            except Exception as e:
                response = { 'status': False, 'message': e}
                return response

    def commit(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            response = { 'status': True, 'message': "sql ejecutado correctamente"}
            return response
        except Exception as e:
            response = { 'status': False, 'message': e}
            return response

    def close(self):
        self.connection.close()
