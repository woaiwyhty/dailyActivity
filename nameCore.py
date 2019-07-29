from gimei import Gimei
from googletrans import Translator
translator = Translator()
# for i in range(0, 1):
#     name = Gimei().name.last.kanji
#     print(name)

#     print('%s %s' % (name, translator.detect(name)))

#print(translator.detect('角松liq facebook検索からコピーして貼り付ければ見れます。 file:///C:/Users/didi/Documents/mqdefault.webp at 東京国税局'))

def getLastName(lang='ja'):
    if lang == 'ja':
        return Gimei().name.last.kanji
    return ''


def detect(body):
    return translator.detect(body)

def analyze(texts, lang='ja'):
    val = 0.0
    try:
        res = detect(texts)
    except Exception as inst:
        print('检测接口调用失败，转入备用方案')
        return 0.9
    if res.lang == lang:
        val = res.confidence
    return val



# print(detect('健人'))
# print(detect('Works at フィットネスインストラクター'))

