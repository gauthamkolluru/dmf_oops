from utils.fetch_engine_package import pkg_details
from ds.sqlserver import SQLSERVER
from dmf_csv.dmf_csv import DMFCSV


DS_TYPES = ['source', 'destination']


def main():
    db_det = pkg_details(DS_TYPES[0])
    src_obj = SQLSERVER(db_det)
    for tbl_name, tbl_keys, tbl_data in src_obj.get_table_data():
        tbl_data.insert(0, tbl_keys)
        csv_obj = DMFCSV(database=db_det['database'],
                         table_name=tbl_name,
                         file_data=tbl_data)
        csv_obj.write_csv()
        csv_obj.split_csv()
    return True


if __name__ == "__main__":
    main()
