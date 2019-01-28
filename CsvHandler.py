import csv
import TimeUtil

def __getList(filepath, read_type):
    list = []
    csv_file = csv.reader(open(filepath,read_type))

    for item in csv_file:
        list.append(item)

    return list

def _writeMD5Csv():
    md5_file = csv.reader(open('D:\git_repo\DesignerWork\designer\Excel\Csv\Md5.csv', 'r'))
    md5_list = __getMD5List()
    for item in md5_list:
        item[2] = TimeUtil._getCurrentTime()

    csv_write = csv.writer(open('D:\git_repo\DesignerWork\designer\Excel\Csv\Md5.csv', 'r+', newline=''))
    for item in md5_list:
        item[2] = TimeUtil._getCurrentTime()
        csv_write.writerow(item)

def _getImportAndExportList():
    list = __getList('ZHRFilepath.csv', 'r')
    return list

def __getMD5List():
    list = __getList('D:\git_repo\DesignerWork\designer\Excel\Csv\Md5.csv', 'r')
    # print(list)
    return list



