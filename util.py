import json
import re
def logMessage(message):
    print(message)



def GetMiddleStr(content,startStr,endStr):
  startIndex = content.index(startStr)
  if startIndex>=0:
    startIndex += len(startStr)
  endIndex = content.index(endStr, startIndex + 1)
  return content[startIndex:endIndex]
def getAccessToken(message):
    res = GetMiddleStr(message, 'access_token\\":\\"', '\\",')
    if len(res) > 0:
        return True, res
    return False, ''
def getUID(message):
    res = GetMiddleStr(message, 'uid\\":', ',')
    if len(res) > 0:
        return True, res
    return False, ''

# print(getAccessToken('[{"code":200,"body":"{\"session_key\":\"5.BegUYqlehZdw4w.1562054052.32-100038706318672\",\"uid\":100038706318672,\"secret\":\"15ef9af49d6eb5b3597373c1477f38b0\",\"access_token\":\"EAAAAUaZA8jlABAHqQtCJlAwO4RTGJ2OMGMuCJdZBtz2WlW4yaGdzEpNZBwEa1NFPc5QooBeVj4LkJsas6kwFLNeeAdh3nwouy4zYqZBFW5XuZBFK5IMApZBzswVXyiM9uCZAGgpG8pKvhZCnq4FFYXsHeCbG1Qbt2dAA7ZBXkobvnk07msumtFH53zeW1fcH0RQsZD\",\"machine_id\":\"pA0bXUWdLddpb5MDb484fJtg\",\"session_cookies\":[{\"name\":\"c_user\",\"value\":\"100038706318672\",\"expires\":\"Wed, 01 Jul 2020 07:54:12 GMT\",\"expires_timestamp\":1593590052,\"domain\":\".facebook.com\",\"path\":\"\\\/\",\"secure\":true},{\"name\":\"xs\",\"value\":\"32:BegUYqlehZdw4w:2:1562054052:-1:-1\",\"expires\":\"Wed, 01 Jul 2020 07:54:12 GMT\",\"expires_timestamp\":1593590052,\"domain\":\".facebook.com\",\"path\":\"\\\/\",\"secure\":true,\"httponly\":true},{\"name\":\"fr\",\"value\":\"3Jae3XFaqASPsUMQX.AWXeDtQIfjIM1Xe-gz5oAe6y3wE.BdGw2k..AAA.0.0.BdGw2k.AWWS2x2q\",\"expires\":\"Wed, 01 Jul 2020 07:54:10 GMT\",\"expires_timestamp\":1593590050,\"domain\":\".facebook.com\",\"path\":\"\\\/\",\"secure\":true,\"httponly\":true},{\"name\":\"datr\",\"value\":\"pA0bXUWdLddpb5MDb484fJtg\",\"expires\":\"Thu, 01 Jul 2021 07:54:12 GMT\",\"expires_timestamp\":1625126052,\"domain\":\".facebook.com\",\"path\":\"\\\/\",\"secure\":true,\"httponly\":true}],\"confirmed\":false,\"identifier\":\" 8618714774628\",\"user_storage_key\":\"ef027d8de3fcc0d2e3c6e21e6f395a8396f03225a6d8a5abe0b67fbade7776c4\"}"},{"code":200,"body":"{\"viewer\":{\"actor\":{\"__type__\":{\"name\":\"User\"},\"id\":\"100038706318672\",\"name\":\"Julieta Chandler\",\"structured_name\":{\"text\":\"Julieta Chandler\",\"parts\":[{\"part\":\"first\",\"offset\":0,\"length\":7},{\"part\":\"last\",\"offset\":8,\"length\":8}]},\"is_mobile_pushable\":false,\"all_phones\":[],\"email_addresses\":[],\"squareProfilePicSmall\":{\"uri\":\"https:\\\/\\\/scontent-atl3-1.xx.fbcdn.net\\\/v\\\/t1.0-1\\\/c25.0.86.86a\\\/p86x86\\\/1379841_10150004552801901_469209496895221757_n.jpg?_nc_cat=1&_nc_oc=AQnbxAxNB8gVUBEv_0_FJxuYh17LqK7wyrXngzmHGyetCGSngX3o-_JZMaxr_dYU4WU&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent-atl3-1.xx&oh=d4361f3fd6557ee70a5f912c7a368cce&oe=5D82439C\",\"width\":86,\"height\":86},\"squareProfilePicBig\":{\"uri\":\"https:\\\/\\\/scontent-atl3-1.xx.fbcdn.net\\\/v\\\/t1.0-1\\\/c43.0.148.148a\\\/p148x148\\\/1379841_10150004552801901_469209496895221757_n.jpg?_nc_cat=1&_nc_oc=AQnbxAxNB8gVUBEv_0_FJxuYh17LqK7wyrXngzmHGyetCGSngX3o-_JZMaxr_dYU4WU&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent-atl3-1.xx&oh=05eab340166ffef6125ea61fb2e197a3&oe=5DBA98D8\",\"width\":148,\"height\":148},\"squareProfilePicHuge\":{\"uri\":\"https:\\\/\\\/scontent-atl3-1.xx.fbcdn.net\\\/v\\\/t31.0-1\\\/c212.0.720.720a\\\/p720x720\\\/1402926_10150004552801901_469209496895221757_o.jpg?_nc_cat=1&_nc_oc=AQnbxAxNB8gVUBEv_0_FJxuYh17LqK7wyrXngzmHGyetCGSngX3o-_JZMaxr_dYU4WU&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent-atl3-1.xx&oh=69334a00c0f376b604b2c6e3fa88dd0c&oe=5DC4AED6\",\"width\":720,\"height\":720},\"profile_picture_is_silhouette\":true,\"is_work_user\":false,\"is_minor\":false,\"is_partial\":false},\"is_fb_employee\":false}}"}]'))