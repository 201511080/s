import os
import requests
import urllib
import mylib 
import lxml
import lxml.etree
from io import StringIO
from urllib.parse import urlencode

def doIt():
    API_URL = "http://openapi-lib.sen.go.kr/openapi/service/lib/openApi"
    # 교수님키
    API_KEY = "8Bx4C1+bogiu3i0M5k7aqOf+TA5yCWK+FDI7nTSJ0oAhDj1NC5CtbI1TMgFmnpuZxJ9LBoCScqBhuw5sul2tmQ=="
    
    NUM_OF_ROWS = 20
    CONTENT_TYPE='json'
    LINE_NUM=str(20)
    
    params = urlencode({
        'serviceKey': API_KEY, 
        'title': '파이썬',
        'manageCd': 'MA',
        'numOfRows': NUM_OF_ROWS,
        'pageNo': 1
    }, doseq=False)
    
    data=requests.get(API_URL + '?' + params).text
    tree=lxml.etree.fromstring(data.encode('utf-8'))
    for node in tree.xpath('//title'):
        print (node.text, end=", ")

if __name__ == "__main__":
    doIt()
