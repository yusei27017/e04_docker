import datetime

header = {}
header[
    'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
header['Accept'] = "application/json, text/plain, */*"
header['Accept-Encoding'] = 'gzip, deflate, br'
header['Accept-Language'] = 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
header['Connection'] = 'keep-alive'
header['Host'] = 'www.104.com.tw'
header['sec-ch-ua'] = '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"'
header['sec-ch-ua-mobile'] = '?0'
header['sec-ch-ua-platform'] = 'macOS"'
header['Sec-Fetch-Dest'] = 'empty'
header['Sec-Fetch-Mode'] = 'cors'
header['Sec-Fetch-Site'] = 'same-origin'

mongo_uri = "mongodb://dev-mongo:27017/"
mongo_search_pipeline = [
    {
        '$sort': {
            'appearDate': -1, 
            'period': 1, 
            'applyCnt': 1, 
            'empCnt': 1
        }
    }, {
        '$project': {
            '_id': 0, 
            'jobName': 1, 
            'periodDesc': 1, 
            'custName': 1, 
            'appearDate': 1, 
            'salaryDesc': 1, 
            'applyCnt': 1, 
            'empCnt': 1, 
            'link.job': 1
        }
    }
]

today = datetime.datetime.today().strftime("%Y%m%d")

def get_header_referer(key_word):
    return f"https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword={key_word}&expansionType=area,spec,com,job,wf,wktm&area=6001001000,6001002000,6001005000&order=14&asc=0&page=1&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"

def get_request_url(key_word, i):
    return f"https://www.104.com.tw/jobs/search/list?ro=0&kwop=7&keyword={key_word}&expansionType=area,spec,com,job,wf,wktm&area=6001001000,6001002000,6001005000&order=15&asc=0&page={i}&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"

def get_referer_for_detail(job_id):
    return {
        "referer": f'https://www.104.com.tw/job/{job_id}jobsource=jolist_a_relevance',
        "ajax_content": f'https://www.104.com.tw/job/ajax/content/{job_id}'
        }
