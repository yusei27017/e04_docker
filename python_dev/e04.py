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
    header['Referer'] = get_header_referer()
    for i in range(1,21):
        condition_url = get_request_url(key_word, i)
        res = sess.get(condition_url, headers=header)
        json_data = json.loads(res.text)['data']        
        for job_log in json_data:
            mongo.insert_job_list(job_log, db_name)
            description_link = job_log['link']['job']
            job_no = job_log['jobNo']
            pattern_str = 'job/([^/]+)'
            check_id = re.findall(pattern_str, description_link)
            if len(check_id) > 0:
                job_id = check_id[0]
                ref_dict = get_referer_for_detail(job_id)
                header['Referer'] = ref_dict['referer']
                ajax_content = ref_dict['ajax_content']
                result = sess.get(ajax_content, headers=header)
                try:
                    json_description = json.loads(result.text)
                    json_description['data']['jobNo'] = job_no
                    mongo.insert_job_description(json_description['data'], db_name)
                except:
                    print(json_description)
    return


if __name__ == "__main__":
    print("start")
    key_word_dict = {
        "GO" : "golang",
        # "Python" : "python"
    }

    for name, key_word in key_word_dict.items():
        condition_search(key_word, name)

    # for db_name, _ in key_word_dict.items():

    #     results = mongo.find_all_data(db_name, today)
    #     for res in results:
    #         company.data_analysis(res, today, db_name)
    print("end")