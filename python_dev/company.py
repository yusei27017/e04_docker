import datetime
import mongo

today_not_format = datetime.datetime.today()
time_format = "%Y%m%d"

def time_diff(tag):
    tag_time = datetime.datetime.strptime(tag, time_format)
    return (tag_time - today_not_format).days

def is_last_appear(date1, date2):
    return datetime.datetime.strptime(date1, time_format) > datetime.datetime.strptime(date2, time_format)

def data_analysis(log_data, date, db_name):
    appear_date = log_data['appearDate']
    comp_log = mongo.find_comp(log_data['custNo'])
    if comp_log:
        match = {"compID": log_data['custNo']}
        if date in comp_log['jobVacancy']:
            comp_log['jobVacancy'][date].append(
                "appear_date:" + appear_date + "|" + "job_no:" +log_data['jobNo'] + "|" + "from:" + db_name
                )
        else:
            comp_log['jobVacancy'][date] = [
                "appear_date:" + appear_date + "|" + "job_no:" +log_data['jobNo'] + "|" + "from:" + db_name
                ]
        if is_last_appear(appear_date, comp_log['lastAppear']):
            comp_log['lastAppear'] = appear_date
        comp_log['jobLog'].append(
            date + '-' + log_data['jobName'] + "(" + log_data['jobNo'] + ")"
            )
        mongo.update_comp_status(match, comp_log)
    else:
        comp_log = {
            "compID" : log_data['custNo'],
            "compName" : log_data['custName'],
            "jobVacancy": {date:[
                "appear_date:" + appear_date + "|" + "job_no:" + log_data['jobNo'] + "|" + "from:" + db_name
                ]},
            "lastAppear" : appear_date,
            "firstAppear": appear_date,
            "jobLog": [
                date + '-' + log_data['jobName'] + "(" + log_data['jobNo'] + ")"
            ]
        }
        mongo.insert_comp_data(comp_log)
    return

if __name__ == "__main__":
    print("start")
    db_array = ["SE", "Backend", "Python", "PHP"]
    for i in range(1, 3):
        day_ago = today_not_format - datetime.timedelta(days=i)
        search_date = day_ago.strftime(time_format)
        for db_name in db_array:
            results = mongo.find_all_data(db_name, search_date)
            for res in results:
                data_analysis(res, search_date, db_name)
