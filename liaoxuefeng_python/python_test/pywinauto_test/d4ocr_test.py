# 初始化OCR
import ddddocr
ocr = ddddocr.DdddOcr()
ocr_beta = ddddocr.DdddOcr(beta=True)  # 切换为第二套ocr模型
filePath="F:/captcha/"

def get_code(fileName: str):
    # image = open("test.jpg", "rb").read()
    # ocr_client.set_ranges("0123456789+-x/=")
    # result = ocr.classification(image, probability=True)
    # s = ""
    # for i in result['probability']:
    #     s += result['charsets'][i.index(max(i))]
    # print(s)
    
    #fileName = filePath+"yzm003.png"
    # 0	纯整数0-9
    # 1	纯小写英文a-z
    # 2	纯大写英文A-Z
    # 3	小写英文a-z + 大写英文A-Z
    # 4	小写英文a-z + 整数0-9
    # 5	大写英文A-Z + 整数0-9
    # 6	小写英文a-z + 大写英文A-Z + 整数0-9
    # 7	默认字符库 - 小写英文a-z - 大写英文A-Z - 整数0-9
    ocr.set_ranges(6)
    image = open(fileName, "rb").read()
    result = ocr.classification(image)
    print(f'OCR识别结果: {result}')
    return(result)

def get_code_beta(fileName: str):
    #fileName = filePath+"yzm003.png"
    ocr_beta.set_ranges(6)
    image = open(fileName, "rb").read()
    result = ocr_beta.classification(image)
    print(f'OCR识别结果: {result}')
    return(result)

def main():
    fileNames = ["F:/captcha/yzm001.png", "F:/captcha/yzm002.png", "F:/captcha/yzm003.png", "F:/captcha/yzm004.png", "F:/captcha/yzm005.png"]
    for fileName in fileNames:
        get_code(fileName)
        get_code_beta(fileName)

if __name__ == '__main__':
    main()