import pdfkit
import xlrd

wkhtmltopdfPath = 'web//wkhtmltopdf//bin//wkhtmltopdf.exe'

# 导入Excle
def impExcle(path,outPath):
    xl = xlrd.open_workbook(path)
    table = xl.sheets()[0]
    rows = table.nrows
    print(rows)
    for i in range(rows):
        if i < 1:
            continue
        row = table.row_values(i)
        print(row)
        url = row[0]
        pdfName = row[1]
        htmltopdf(url,pdfName,outPath)

def htmltopdf(url,pdfName,outPath):
    confg = pdfkit.configuration(wkhtmltopdf=wkhtmltopdfPath)
    # 这里指定一下wkhtmltopdf的路径，这就是我为啥在前面让记住这个路径
    pdfkit.from_url(url, outPath + '/' + pdfName + '.pdf', configuration=confg)

def buildpdf(url,pdfName,outPath):
    htmltopdf(url,pdfName,outPath)
    return "ok"

# if __name__ == '__main__':
#     # 导入表格
#     impExcle(r"test1.xlsx")