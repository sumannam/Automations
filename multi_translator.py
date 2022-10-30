from googletrans import Translator
# pip install googletrans==3.1.0a0
import requests


source_file = r"D:\Git\utils\orgin_paper.txt"

def MergeLine():
    eng_text = ""
    file = open(source_file, "r", encoding='UTF8')
    lines = file.readlines()

    for line in lines:
        code =line.strip('\n') 
        eng_text = eng_text + " " + code

    file.close()

    return eng_text


def googleTrnas(eng_text):
    translator = Translator()
    trans_text =  translator.translate(eng_text, dest='ko')
    return trans_text


def kakaoTrans(eng_text):
    url = "https://translate.kakao.com/translator/translate.json"

    headers = {
        "Referer": "https://translate.kakao.com/",
        "User-Agent": "Mozilla/5.0"
    }

    data = {
        "queryLanguage": "en",
        "resultLanguage": "kr",
        "q": eng_text
    }
    
    resp = requests.post(url, headers=headers, data=data)
    data = resp.json()
    trans_text = data['result']['output']
    return trans_text

def printKakaoTrans(ko_text):
    for line in ko_text:
        print(line, end=' ')

if __name__ == "__main__":
    eng_text = MergeLine()
    google_trans_text = googleTrnas(eng_text)
    kakao_trans_text = kakaoTrans(eng_text)


    print(google_trans_text.origin)
    print("=== Google Translator ===")
    print(google_trans_text.text)
    print("=== Kakao Translator ===")
    print(printKakaoTrans(kakao_trans_text[0]))



