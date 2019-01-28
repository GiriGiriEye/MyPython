import X2CCsv
import CsvHandler as csvHandler

# def xlsx_to_csv():
    # filepath_list = getList()
    # for item in filepath_list:
    #     x2c.xlsx_to_csv(item[0],item[1])

# def getCSVList():
#
def exportMD5():
    csvHandler._writeMD5Csv()

if __name__ == '__main__':
    # xlsx_to_csv()
    x2c = X2CCsv.X2CCsv
    for item in csvHandler._getImportAndExportList():
        x2c.xlsx_to_csv(list=item)
    exportMD5()