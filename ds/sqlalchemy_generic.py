from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.url import URL as connection_url


class SQLALCHEMY_GENERIC:
    def __init__(self, drivername="", username="", password="", host="", port=0, database="", connection_query=dict()):
        self.drivername = drivername
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.query = connection_query
        self.conn_string = repr(connection_url(self.drivername,
                                               username=self.username,
                                               password=self.password,
                                               host=self.host,
                                               port=self.port,
                                               database=self.database,
                                               query=self.query))
        self.db_conn = create_engine(self.conn_string)
        self.select_query = "select * from {}"
        self.table_names = self.db_conn.table_names()

    def get_table_data(self):
        for table_name in self.table_names:
            self.table_data = self.db_conn.execute(
                self.select_query.format(table_name))
            yield self.table_data.keys(), self.table_data.fetchall()


if __name__ == '__main__':

    def pkg_details(ds_type):
        import json
        with open("./settings.json", "r") as sj:
            setting_list = json.load(sj)
        return setting_list["db_engines"][ds_type] if setting_list else False

    db_det = pkg_details('source')

    sag = SQLALCHEMY_GENERIC(db_det['drivername'],
                             username=db_det['username'],
                             password=db_det['password'],
                             host=db_det['host'],
                             port=db_det['port'],
                             database=db_det['database'],
                             connection_query={"driver": "sql+server"})
    for k, d in sag.get_table_data():
        print(k)
        print(d)
