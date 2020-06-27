from utils.fetch_engine_package import pkg_details
from ds import sqlserver
from dmf_csv import dmf_csv


DS_TYPES = ['source', 'destination']


def main():
    db_det = pkg_details(DS_TYPES[0])
    # src_obj = sqlserver.SQLSERVER(db_det)
    print(dir(sqlserver))
    # print(src_obj.print_values())
    return True


if __name__ == "__main__":
    main()
