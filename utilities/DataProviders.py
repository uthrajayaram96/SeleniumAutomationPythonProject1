"""
This file gets/reads all the data from the LoginTestData.xlsx file

"""
from utilities.ExcelUtility import ExcelUtility


class DataProviders:

    @staticmethod
    def get_test_data(file_name):
        excel_reader = ExcelUtility(file_name, 'Sheet1')
        testdata = []

        row_cnt = excel_reader.get_row_count()
        col_cnt = excel_reader.get_column_count()

        for i in range(2, row_cnt + 1):
            data = []
            for j in range(1, col_cnt + 1):
                data.append(excel_reader.read_data_from_cell(i, j))
            testdata.append(data)

        return testdata
