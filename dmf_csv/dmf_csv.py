import csv
from fsplit.filesplit import FileSplit

FILE_EXT = "csv"
# 1GB in bytes, approx
# SPLIT_SIZE = 1000000000
SPLIT_SIZE = 10


class DMFCSV:
    def __init__(self, database="", table_name="", file_data=[]):
        self.__file_name = "_".join([database, table_name])
        self.__data = file_data

    def write_csv(self):
        with open(".".join([self.__file_name, FILE_EXT]), 'w') as csvfile:
            self.__data_writer = csv.writer(csvfile)
            self.__data_writer.writerows(self.__data)
        return True

    def split_csv(self):
        self.__fs = FileSplit(file=".".join(
            [self.__file_name, FILE_EXT]), splitsize=SPLIT_SIZE)
        return self.__fs.split(include_header=True)
