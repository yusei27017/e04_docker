import pymongo
import os, csv

from env import mongo_uri, mongo_search_pipeline, today

conn = pymongo.MongoClient(mongo_uri, 27017)
db = conn.E04

def export_to_csv(db_name):
    col_name = "jobList" + db_name + today
    col = db[col_name]
    # 執行聚合查詢
    results = col.aggregate(mongo_search_pipeline)
    # 指定CSV文件名稱
    csv_name = f'{col_name}.csv'
    csv_file = os.path.join("./data", csv_name)
    # 將結果寫入CSV文件
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 寫入欄位標題
        writer.writerow(['jobName', 'periodDesc', 'custName', 'appearDate', 'salaryDesc', 'applyCnt', 'empCnt', 'link.job'])
        # 寫入查詢結果
        for result in results:
            writer.writerow([
                result['jobName'],
                result['periodDesc'],
                result['custName'],
                result['appearDate'],
                result['salaryDesc'],
                result['applyCnt'],
                result['empCnt'],
                result['link']['job']
            ])
    return

def insert_job_list(log, db_name):
    col_name = "jobList" + db_name + today
    col = db[col_name]
    res = col.insert_one(log)
    print(res)
    return

def insert_job_description(log, db_name):
    col_name = "jobDescription" + db_name + today
    col = db[col_name]
    res = col.insert_one(log)
    print(res)
    return

def insert_comp_data(log):
    col_name = "compList"
    col = db[col_name]
    res = col.insert_one(log)
    print(res)
    return

def update_comp_status(tag, log):
    col_name = "compList"
    col = db[col_name]
    update_log = {"$set": log}
    res = col.update_one(tag, update_log)
    print(res)
    return

def find_job(db_name):
    col_name = "jobList" + db_name + today
    col = db[col_name]
    results = col.find()
    for result in results:
        print(result['tags'])
    return

def find_all_data(db_name, date):
    col_name = "jobList" + db_name + date
    col = db[col_name]
    results = col.find()
    return results

def find_comp(comp_id):
    col_name = "compList"
    col = db[col_name]
    result = col.find_one({'compID':comp_id})
    return result

def global_search_by_jobNo(jobNo):
    show_dbs = ["SE", "Backend", "Python", "PHP", "DevOps"]
    for db_name in show_dbs:
        col_name = "jobList" + db_name + today
        col = db[col_name]
        result = col.find({'jobNo':jobNo})
        print("from: "+db_name)
        for info in result:
            print(info)
    return
    

if __name__ == "__main__":
    # find_job('Backend')
    # {'compName':{$regex:"倍特.*"}}
    global_search_by_jobNo("12512671")
    print('end')