from urllib import request
from urllib import parse
import util
import uuid
import random
import time
import json
from socket import *
from imageGenerate import imageGenerate
from configparser import ConfigParser
import ssl

class fbFriendsAdder():
    m_imageGenerate = None
    opener = None
    deviceid = ''
    sessionID = ''
    password = ''
    phone = ''
    originPhone = ''
    userid = ''
    token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    authToken = ''
    uploadStrPacket = ''
    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X)[FBAN/FB4A;FBAV/42.0.0.27.114;FBPN/com.facebook.katana;FBLC/en_US;FBBV/14063944;FBCR/T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBDV/ONEPLUS A5000;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=1600,height=900};FB_FW/1;]',
        'X-FB-Connection-Type': 'WIFI',
        'x-fb-net-hni': '',
        'x-fb-sim-hni': '',
        'X-FB-HTTP-Engine': 'Apache',
        'Transfer-Encoding': 'chunked',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive'
    }
    def __init__(self, uploadStrPacket, imageGen, username, password, deviceid = '', authToken = ''):
        # multiprocessing.Process.__init__(self)
        self.uploadStrPacket = uploadStrPacket
        self.m_imageGenerate = imageGen
        self.phone = username
        self.password = password
        if deviceid == '':
            deviceid = uuid.uuid1().__str__()
        self.authToken = authToken
        self.deviceid = deviceid
        random.seed()

    def waitRandom(self):
        for i in range(1, 2):
            time.sleep(random.random())
    def waitPeriod(self, a, b):
        for i in range(a, b):
            time.sleep(random.random())
    def headerTemplate(self):
        return {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X)[FBAN/FB4A;FBAV/42.0.0.27.114;FBPN/com.facebook.katana;FBLC/en_US;FBBV/14063944;FBCR/T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBDV/ONEPLUS A5000;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=1600,height=900};FB_FW/1;]',
            'X-FB-Connection-Type': 'WIFI',
            'x-fb-net-hni': '',
            'x-fb-sim-hni': '',
            'X-FB-HTTP-Engine': 'Apache',
            'Transfer-Encoding': 'chunked',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive'
        }

    def setup(self, ipuser = 'sp06986840', ippass = 'wyhty2627',
                 ipdomain = 'us.smartproxy.com', ipport = '10000'):
        for i in range(0, 3):
            try:
                self.opener = request.build_opener(request.ProxyHandler(
                    {
                        'http': 'http://%s:%s@%s:%s' % (ipuser, ippass, ipdomain, ipport),
                        'https': 'http://%s:%s@%s:%s' % (ipuser, ippass, ipdomain, ipport),
                    }
                ))
                # self.opener = request.build_opener(request.ProxyHandler(
                #     {
                #         'http': 'http://192.168.0.11:8888',
                #         'https': 'http://192.168.0.11:8888',
                #     }
                # ))
                # self.opener = request.build_opener(request.ProxyHandler(
                #     {
                #         'http': 'http://YYVsg2:eg31Ys@168.235.71.168:40614',
                #         'https': 'https://YYVsg2:eg31Ys@168.235.71.168:40614',
                #     }
                # ))
                print('开始测IP')
                print(self.opener.open('http://lumtest.com/myip.json', timeout=5).read())
                print('初始化注册成功')
                break
            except Exception as inst:
                print('IP获取失败, 开始重试')



    def login(self):
        self.sessionID = uuid.uuid1().__str__()
        url = 'https://api.facebook.com/method/logging.clientevent'
        message = '{"time":1562474285756,"app_ver":"42.0.0.27.114","build_num":14063944,"session_id":"{sessionID}","seq":0,"uid":null,"tier":"regular","app_id":"350685531728","device_id":"{deviceID}","carrier":"中国移动","device":"MuMu","os_ver":"6.0.1","conn":"WIFI","sent_time":"1562474295.127","config_checksum":"","config_version":"v2","data":[{"time":"1562474285.756","log_type":"client_event","name":"app_new_install","extra":{"tracking_enabled":true,"process":"com.facebook.katana"},"bg":true},{"time":"1562474291.68","log_type":"client_event","name":"marauder_beacon","module":"marauder","extra":{"impl":"analytics1","tier":"regular","beacon_id":1,"process":"com.facebook.katana"}},{"time":"1562474285.788","log_type":"client_event","name":"navigation","module":"unknown","extra":{"dest_module":"login_screen","click_point":"foreground","dest_module_class":"FacebookLoginActivity","activity_stack_size":1,"process":"com.facebook.katana"}}]}'
        message = message.replace('{sessionID}', self.sessionID).replace('{deviceID}', self.deviceid)
        dataMap = {
            'message' : message,
            'compressed': '0',
            'format': 'json',
            'locale': 'en_US',
            'client_country_code': 'US',
            'method': 'logging.clientevent',
            'fb_api_req_friendly_name': 'sendAnalyticsLog',
            'fb_api_caller_class': 'com.facebook.analytics.service.AnalyticsQueue',
            'access_token': self.token,
        }
        newHeaders = self.headerTemplate()
        newHeaders['Authorization'] = 'OAuth null'
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request(url, headers=newHeaders, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()

    def getMachineID(self):
        arr = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ-zyxwvutsrqponmlkjihgfedcba', 24)
        return ''.join(arr)
    def getBatch(self):
        machineID = self.getMachineID()
        batch = '[{"method":"POST","body":"format=json&device_id='+self.deviceid+'&email='+self.phone+'&password='+self.password+'&credentials_type' \
                                                                                 '=password&generate_session_cookies=1&error_detail_type=button_with_disabled&machine_id='+machineID+'&locale=en_US&client_country_code=US&fb_api_req_friendly_name=authenticate","name":"authen' \
                'ticate","omit_response_on_success":false,"relative_url":"method/auth.login"},{"method":"POST","body":"query_params=%7B%220%22%3A84%2C%221%22%3A135%2C%222%22%3A540%7D&method=get&query_id=10153437257771729&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=GetLoggedInUserQuery","name":' \
                '"getLoggedInUser","depends_on":"authenticate","omit_response_on_success":false,"relative_url":"graphql?' \
                'access_token={result=authenticate:$.access_token}"}]'
        return batch

    def OAuth(self):
        newHeader = self.headerTemplate()
        newHeader['Authorization'] = 'OAuth %s' % (self.token)
        dataMap = {
            'batch' : self.getBatch(),
            'fb_api_caller_class' : 'com.facebook.katana.server.handler.Fb4aAuthHandler',
            'fb_api_req_friendly_name' : 'authLogin'
        }
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request('https://b-graph.facebook.com/?include_headers=false&locale=en_US&client_country_code=US', headers=newHeader, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()
        page = page.decode('utf-8')
        print(page)
        if page.find('User must verify their account on www.facebook.com') != -1:
            raise Exception('账号需要审核')
        boolRes, self.authToken = util.getAccessToken(page)
        if boolRes == False:
            raise Exception('获取access token失败')
        boolRes, self.userid = util.getUID(page)
        if boolRes == False:
            raise Exception('获取UID失败')

    def searchWords(self):
        words = [
            {
                'name' : 'Rakuten, Inc',
                'id' : '113926781984735'
            },
            {
                'name': 'Facebook navi',
                'id': '211790478849971'
            },
            {
                'name': 'BBC NEWS',
                'id': '228735667216'
            },
            {
                'name': 'PECO［',
                'id': '399909446834300'
            },
            {
                'name': 'SHISEIDO',
                'id': '203899256723268'
            },
            {
                'name': 'WATCHY FOOD',
                'id': '1547889158574617'
            }
        ]
        return random.choice(words)

    def searchMainPage(self, keyword):
        url = 'https://graph.facebook.com/graphql'
        dataMap = {
            'query_params': '{"0":"%s","3":"10","1":"page","4":"101"}' % keyword,
            'method': 'get',
            'query_id': '10153280114911729',
            'strip_nulls': 'true',
            'strip_defaults': 'true',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'FetchSimpleSearchEntitiesQuery',
            'fb_api_caller_class': 'com.facebook.search.protocol.FetchSimpleSearchEntitiesGraphQLModels$FetchSimpleSearchEntitiesQueryModel',
        }
        newHeaders = self.headerTemplate()
        newHeaders['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request(url, headers=newHeaders, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()
        res = json.loads(page)
        if keyword in res:
            res = res[keyword]
            if 'search_results' in res:
                res = res['search_results']
                if 'edges' in res:
                    res = res['edges']
                    return True, res
        return False, page
    def searchLog(self, keyword, name, id):
        url = 'https://api.facebook.com/method/mobilesearchactivitylog'
        dataMap = {
            'search_type': 'simple_search',
            'message': '{"user_input":"%s","selected_type":"Page","selected_text":"%s","selected_semantic":"%s","timestamp":%s}' % (keyword, name, id, time.time()),
            'locale': 'en_US',
            'client_country_code': 'US',
            'method': 'mobilesearchactivitylog',
            'fb_api_req_friendly_name': 'mobilesearchactivitylog',
            'fb_api_caller_class': 'com.facebook.search.service.GraphSearchLogQueue',
        }
        newHeaders = self.headerTemplate()
        newHeaders['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request(url, headers=newHeaders, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()
        print(page.decode('utf-8'))

    def openMainPage(self, id):
        url = 'https://graph.facebook.com/graphql'
        queryParam = '{"11":68,"0":"{pageID}","2":810,"12":68,"6":559,"5":1080,"14":"true","15":"2","32":"2","35":"4","21":"profile","33":"page_only","3":"image/jpeg","13":"image/x-auto","25":"contain-fit","23":1080,"24":2048,"28":540,"29":2048,"26":122,"27":2048,"30":21,"31":2048}'
        queryParam = queryParam.replace('{pageID}', id)
        dataMap = {
            'query_params' : queryParam,
            'method': 'get',
            'query_id': '10153948982466729',
            'strip_nulls': 'true',
            'strip_defaults': 'true',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'TimelineFirstUnitsPage',
            'fb_api_caller_class': 'com.facebook.pages.identity.timeline.PageIdentityInfinitePostsTimelineFragment',
        }
        newHeaders = self.headerTemplate()
        newHeaders['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request(url, headers=newHeaders, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()
        res = json.loads(page)
        if id in res:
            res = res[id]
            if 'firstSection' in res:
                res = res['firstSection']['nodes'][0]['timeline_units']['edges']
                return True, res
        return False, page

    def like(self, id, tracking):
        url = 'https://graph.facebook.com/%s/likes' % id
        dataMap = {
            'tracking': tracking,
            'nectar_module': 'pages_identity_ufi',
            'feedback_source': 'pages_native_timeline',
            'format': 'json',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'graphObjectLike',
            'fb_api_caller_class': 'com.facebook.feed.protocol.UFIQueue',
        }
        newHeaders = self.headerTemplate()
        newHeaders['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request(url, headers=newHeaders, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()
        return page.decode('utf-8')

    def share(self, sharedID, tracking):
        url = 'https://graph.facebook.com/?include_headers=false&decode_body_json=false&streamable_json_response=true&locale=en_US&client_country_code=US'
        tracking = tracking.replace('"', '\\"')
        tracking = '["%s"]' % tracking
        tracking = parse.quote(tracking, 'utf-8')
        batch = '[{"method":"POST","body":"privacy=%7B%22value%22%3A%22EVERYONE%22%7D&composer_session_id={sessionID}&qn={sessionID}&audience_exp=true&attach_place_suggestion=false&format=json&id={shareableID}&to={userID}&tracking={tracking}&locale=en_US&client_country_code=US&fb_api_req_friendly_name=graphObjectShare","name":"graphObjectShares","omit_response_on_success":false,"relative_url":"sharedposts"},{"method":"POST","body":"query_params=%7B%2211%22%3A68%2C%220%22%3A%22%7Bresult%3DgraphObjectShares%3A%24.id%7D%22%2C%222%22%3A810%2C%2212%22%3A68%2C%2214%22%3A%222%22%2C%2220%22%3A%22feed%22%2C%2221%22%3A%22false%22%2C%22max_facepile_reactors%22%3A20%2C%223%22%3A%22image%2Fjpeg%22%2C%2213%22%3A%22image%2Fx-auto%22%2C%2224%22%3A%22contain-fit%22%2C%2222%22%3A1080%2C%2223%22%3A2048%2C%2227%22%3A540%2C%2228%22%3A2048%2C%2225%22%3A122%2C%2226%22%3A2048%2C%2229%22%3A21%2C%2230%22%3A2048%2C%226%22%3A559%2C%225%22%3A1080%2C%22enable_ranked_replies%22%3A%22true%22%2C%22enable_private_reply%22%3A%22true%22%2C%22enable_comment_replies_single_most_recent%22%3A%22false%22%2C%22enable_comment_replies_most_recent%22%3A%22true%22%2C%22enable_comment_replies_least_recent%22%3A%22false%22%2C%22max_comment_replies%22%3A3%2C%2219%22%3A%22true%22%2C%2221%22%3A%22false%22%2C%22max_facepile_reactors%22%3A20%7D&method=get&query_id=10153948981786729&strip_nulls=true&strip_defaults=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=StaticGraphQlPlatformStoryQuery","name":"fetchShare","omit_response_on_success":false,"relative_url":"graphql"}]'
        uuidStr = uuid.uuid1().__str__()
        batch = batch.replace('{sessionID}', uuidStr).replace('{userID}', self.userid).replace('{shareableID}', sharedID).replace('{tracking}', tracking)
        dataMap = {
            'batch' : batch,
            'fb_api_caller_class': 'com.facebook.composer.publish.ComposerPublishServiceHandler',
            'fb_api_req_friendly_name': 'publishShare',
        }
        newHeaders = self.headerTemplate()
        newHeaders['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request(url, headers=newHeaders, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()
        return page.decode('utf-8')

    def getUserID(self):
        url = 'https://b-api.facebook.com/method/bookmarks.get'
        dataMap = {
            'format': 'JSON',
            'one_column': 'true',
            'icon_style': 'caspian',
            'locale': 'en_US',
            'client_country_code': 'US',
            'method': 'bookmarks.get',
            'fb_api_req_friendly_name': 'bookmarkSync',
            'fb_api_caller_class': 'com.facebook.bookmark.client.BookmarkSyncQueue',
        }
        newHeader = self.headerTemplate()
        newHeader['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request(url, headers=newHeader, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()
        page = page.decode('utf-8')
        print(page)
        res = json.loads(page)
        if page.find('Error validating access token: The user is enrolled in a blocking') != -1:
            raise Exception('账号需要审核')
        return res[0]['all'][0]['id']

    def run(self):
        try:
            self.setup(ipuser, ippass, ipdomain, ipport)
            if len(self.authToken) < 10:
                self.login()
                self.OAuth()
            else:
                print('已经有令牌, 直接开始获取用户ID')
                m_friend.userid = self.getUserID()
                print(m_friend.userid)
            likeNum = random.randint(2, 5)
            shareNum = random.randint(2, 5)
            likeCnt = 0
            shareCnt = 0
            print('登录成功, 计划点赞 %s 次, 分享 %s 次' % (likeNum, shareNum))
            for i in range(0, 1):
                if likeCnt >= likeNum or shareCnt >= shareNum:
                    break

                word = self.searchWords()
                print('当前关键字为: %s' % word['name'])
                print('开始搜索主页')
                a, b = self.searchMainPage(word['name'])
                if a == False:
                    print('搜索主页失败...准备重试')
                    self.waitPeriod(1, 3)
                    continue
                success = False

                for j in b:
                    if j['node']['id'] == word['id']:
                        self.searchLog(word['name'], j['node']['name'], j['node']['id'])
                        print('搜索主页成功, 开始打开主页')
                        success = True
                if success == False:
                    print('搜索主页失败')
                    continue
                a, b = self.openMainPage(word['id'])
                if a == False:
                    print('打开主页失败...准备重试')
                    self.waitPeriod(1, 3)
                    continue
                print('打开主页成功, 开始点赞和分享')
                if likeCnt < likeNum:
                    for i in b:
                        if likeCnt >= likeNum or shareCnt >= shareNum:
                            break
                        tracking = i['node']['tracking']
                        shareID = i['node']['shareable']['id']
                        storyID = i['node']['legacy_api_story_id']
                        if random.randint(0, 1) == 0:
                            print('随机概率不成功，不点赞')
                        else:
                            print('随机概率成功, 开始点赞')
                            res = self.like(storyID, tracking)
                            if res == 'true':
                                likeCnt = likeCnt + 1
                                print('点赞成功, 延迟...')
                                self.waitPeriod(1, 3)
                        if random.randint(0, 1) == 0:
                            print('随机概率不成功，不分享')
                        else:
                            print('随机概率成功, 开始分享')
                            res = self.share(shareID, tracking)
                            if res.find('"code":200') != -1:
                                shareCnt = shareCnt + 1
                                print('分享成功, 延迟...')
                                self.waitPeriod(1, 3)
            print('当前账号操作成功')
            return '当前账号操作成功'
        except Exception as e:
            print(e.args)
            if len(e.args) > 0 and e.args[0] == '账号需要审核':
                return '账号需要审核'
            return '操作失败'

if __name__ == '__main__':
    #
    # m_imageGenerate = imageGenerate('profilephoto')
    # m_friend = fbFriendsAdder('', m_imageGenerate, '8615943581749', 'nghk5KfuHo')
    #
    # m_friend.setup()
    # m_friend.login()
    # m_friend.OAuth()
    # word = m_friend.searchWords()
    # a, b = m_friend.searchMainPage(word['name'])
    # a, b = m_friend.openMainPage(word['id'])
    # print(a)
    # print(b)
    # tracking = b[0]['node']['tracking']
    # shareID = b[0]['node']['shareable']['id']
    # storyID= b[0]['node']['legacy_api_story_id']
    # print(tracking)
    # print(shareID)
    # print(storyID)
    # # print(m_friend.like(storyID, tracking))
    #
    # print(m_friend.share(shareID, tracking))
    # exit()

    print('开始')
    time.sleep(1)
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        cp = ConfigParser()
        cp.read("peizhi.cfg", encoding='utf-8')
        ipuser = cp.get('ip', 'ipUser')
        ippass = cp.get('ip', 'ipPass')
        ipdomain = cp.get('ip', 'ipDomain')
        ipport = cp.get('ip', 'ipPort')
        serverIP = cp.get('others', 'serverIP')
        time.sleep(1)
        m_imageGenerate = imageGenerate('profilephoto')
        tcp_client_socket = socket(AF_INET, SOCK_STREAM)
        time.sleep(1)
        print('开始连接')
        tcp_client_socket.connect((serverIP, 19750))
    except Exception as inst:
        print("线程初始化失败, 请重新开启")
        exit()

    BUFSIZE = 65535
    print('连接加好友服务器成功, 开始等待账号')
    while True:
        tcp_client_socket.send(b'RequestAccount|')
        data = tcp_client_socket.recv(BUFSIZE).decode('gbk')
        if not data:
            print('与服务器断开连接')
            break
        # print('得到账号 %s' % data)

        arr = data.split('\t')
        print(data)
        m_friend = fbFriendsAdder('', m_imageGenerate, arr[1], arr[2], arr[3], arr[4])
        res = m_friend.run()

        sendData = 'FinishAccount|%s|%s|%s' % (arr[0], res, m_friend.authToken)
        tcp_client_socket.send(sendData.encode(encoding='gbk'))
        print('操作完成, 继续等待新的账号')
        time.sleep(2)

    tcp_client_socket.close()
