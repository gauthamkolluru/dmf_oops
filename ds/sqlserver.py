# from sqlalchemy_generic import SQLALCHEMY_GENERIC
from . import sqlalchemy_generic

QUERY_STRING = {"driver": "sql+server"}


class SQLSERVER(sqlalchemy_generic.SQLALCHEMY_GENERIC):
    def __init__(self, db_details):
        self.db_details = db_details
        self.connection_query = self.db_details["connection_query"].update(
            QUERY_STRING) if self.db_details["connection_query"] else QUERY_STRING
        super().__init__(drivername=self.db_details["drivername"],
                         username=self.db_details["username"],
                         password=self.db_details["password"],
                         host=self.db_details["host"],
                         port=self.db_details["port"],
                         database=self.db_details["database"],
                         connection_query=self.connection_query)

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

    ss = SQLSERVER(db_det)

    for k, d in ss.get_table_data():
        print(k)
        print(d)
