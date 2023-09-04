import requests
import re
import json
import mongo
import company
from env import header, today, get_header_referer, get_request_url, get_referer_for_detail

sess = requests.Session()

def write_in_local(data, fileName):
    with open(fileName, "a") as write_file:
        json.dump(data, write_file, ensure_ascii=False, indent=4)
    return

def condition_search(key_word, db_name):
    header['Referer'] = get_header_referer(key_word)
    for i in range(1,31):
        condition_url = get_request_url(key_word, i)
        res = sess.get(condition_url, headers=header)
        json_data = json.loads(res.text)        
        job_data = json_data['data']['list']
        for job_log in job_data:
            if not job_log['tags'] or 'emp' not in job_log['tags']:
                job_log['empCnt'] = 0
            else:
                emp_cnt = re.findall('員工(.*?)人',job_log['tags']['emp']['desc'])[0]
                job_log['empCnt'] = int(emp_cnt)
            mongo.insert_job_list(job_log, db_name)
            description_link = job_log['link']['job']
            job_no = job_log['jobNo']
            pattern_str = 'job/(.*?)jobsource'
            check_id = re.findall(pattern_str, description_link)
            if check_id:
                job_id = check_id[0]
                ref_dict = get_referer_for_detail(job_id)
                header['Referer'] = ref_dict['referer']
                ajax_content = ref_dict['ajax_content']
                result = sess.get(ajax_content, headers=header)
                json_description = json.loads(result.text)
                json_description['data']['jobNo'] = job_no
                mongo.insert_job_description(json_description['data'], db_name)
    return


if __name__ == "__main__":
    print("start")
    key_word_dict = {
        # "SE" : "Software%20Engineer",
        # "Backend" : "Backend%20Engineer",
        # "Python" : "python",
        "PHP" : "php",
        # "DevOps": "DevOps"
    }
    
    for name, key_word in key_word_dict.items():
        condition_search(key_word, name)

    for _, db_name in key_word_dict.items():

        results = mongo.find_all_data(db_name, today)
        for res in results:
            company.data_analysis(res, today, db_name)
    print("end")