from sqlalchemy_generic import SQLALCHEMY_GENERIC

QUERY_STRING = {"driver": "sql+server"}


class SQLSERVER(SQLALCHEMY_GENERIC):
    def __init__(self, drivername="", username="", password="", host="", port=0, database="", connection_query=QUERY_STRING):
        super().__init__(drivername, username, password,
                         host, port, database, connection_query)

    def print_values(self):
        print(self.drivername)
        print(self.username)
        print(self.password)
        print(self.host)
        print(self.port)
        print(self.database)
        print(self.query)
        print(self.conn_string)
        print(self.db_conn)
        print(self.select_query)
        print(self.table_names)


if __name__ == "__main__":

    def pkg_details(ds_type):
        import json
        with open("./settings.json", "r") as sj:
            setting_list = json.load(sj)
        return setting_list["db_engines"][ds_type] if setting_list else False

    db_det = pkg_details('source')

    ss = SQLSERVER(db_det['drivername'],
                   username=db_det['username'],
                   password=db_det['password'],
                   host=db_det['host'],
                   port=db_det['port'],
                   database=db_det['database'])
    # ss.print_values()

    for k, d in ss.get_table_data():
        print(k)
        print(d)
