from urllib import request
class smsReceiver:
    __userName = ''
    __passWord = ''
    __token = ''
    def __init__(self, username, password):
        self.__userName = username
        self.__passWord = password

    def login(self):
        apiUrl = 'http://api.jmyzm.com/http.do?action=loginIn&uid=%s&pwd=%s' % (self.__userName, self.__passWord)
        res = request.urlopen(url=apiUrl, timeout=10).read().decode('utf-8').split('|')
        if len(res) == 2:
            self.__token = res[1]
            return True
        else:
            return False

    def getMobileNum(self, id):
        apiUrl = 'http://api.jmyzm.com/http.do?action=getMobilenum&uid=%s&pid=%s&token=%s&vno=0&operator=CMCC' % (self.__userName, id, self.__token)
        res = request.urlopen(url=apiUrl, timeout=15).read().decode('utf-8')
        resArr = res.split('|')
        if len(resArr) == 2 and res.find('to_fast_try_again')== -1:
            return resArr[0], True
        else:
            return res, False

    def getVcodeAndReleaseMobile(self, mobile):
        apiUrl = 'http://api.jmyzm.com/http.do?action=getVcodeAndReleaseMobile&uid=%s&mobile=%s&token=%s' % (self.__userName, mobile, self.__token)
        res = request.urlopen(url=apiUrl, timeout=15).read().decode('utf-8')
        resArr = res.split('|')
        if len(resArr) == 2 and res.find('to_fast_try_again')== -1:
            return resArr[1], True
        else:
            return res, False


# m_smsReceiver = smsReceiver('wh188520', 'qaz810830')
# print(m_smsReceiver.login())
#
# print(m_smsReceiver.getMobileNum('1382'))

