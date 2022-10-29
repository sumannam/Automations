import googletrans
# pip install googletrans

source_file = r"D:\Git\utils\orgin_paper.txt"

eng_text = ""

file = open(source_file, "r", encoding='UTF8')
lines = file.readlines()
for line in lines:
    code =line.strip('\n') 
    eng_text = eng_text + " " + code
    # print(code)
file.close()

translator = googletrans.Translator()
kor_text =  translator.translate(eng_text, src='en', dest='ko')

print(eng_text)
print(kor_text)