# coding: utf-8
import os
import urllib
import requests
import mylib

def doIt():
    _d=dict()
    _d['title']='도둑' 
    _d['manageCd']='MA'
    _d['numOfRows']='5'
    _d['pageNo']='2'
    params2 = urllib.parse.urlencode(_d)

    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    params='?'+'serviceKey='+key['gokr']+'&'+params2

    _url = 'http://openapi-lib.sen.go.kr/openapi/service/lib/openApi'
    url=urllib.parse.urljoin(_url,params)
    data=requests.get(url).text
    print (data)

if __name__ == "__main__":
    doIt()
