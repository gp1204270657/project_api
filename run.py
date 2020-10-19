from httprunner.api import HttpRunner
from httprunner.report import gen_html_report
import requests
import json

def run_test():
    http=HttpRunner()
    http.run('testcase_prod')
    res=http._summary
    return res

def sendtext():
    res=run_test()
    respoens=res.get("stat")
    result=str(respoens)
    url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2330f4ce-434b-4fd0-bba3-17bb612e88be"
    data={
    "msgtype": "text",
    "text": {
    "content": result
  }
}
    res=requests.post(url,json=data)
    return res


if __name__ == '__main__':
    sendtext()