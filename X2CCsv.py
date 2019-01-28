import pandas as pd
import X2C

class X2CCsv(X2C.X2C):

    def xlsx_to_csv(list):
        xlsx = list[0]
        csv = list[1]
        client_csv = list[2]
        data_xls = pd.read_excel(xlsx,header = None,index=0)

        #这一句会把两行表头删掉
        # data_xls = data_xls.drop([0,1])

        data_xls.to_csv(csv, encoding='gb2312',header=None,index=False)

        # 这一句会把两行表头删掉
        data_xls = data_xls.drop([0,1])
        data_xls.to_csv(client_csv, encoding='gb2312',header=None,index=False)
        print(data_xls)


