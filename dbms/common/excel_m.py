import  xlwings

def  main():
    #xlwings 통해 Workbook 호출
    wb = xlwings.Book.caller()

    #Sheet 설정
    sheet = wb.sheets[0]

    #텍스트 입력
    sheet["A1"].value = "xlwings code"
    sheet["A2"].value = "test"

if  __name__== "__main__":
    #path = r"C:\Users\Desktop\VS CODE\Project\practice"
    path = r"C:\MyWork\03. Project\06. 시험"
    #매크로 파일 설정
    xlwings.Book(path+"/"+"p1.xlsm").set_mock_caller()
    #main 함수 호출
    main()