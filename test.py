import json

import sql_db

sql = "select text,id from url "
conn = sql_db.sqlconn()
rows = sql_db.sql_read(sql, conn)
k=0
for i in rows['rows']:
    print(i[1])
    temp = i[0][149:-20]
    temp = json.loads(temp)

    if temp['zpData'].get('jobList',0) != 0 :
        for j in temp['zpData']['jobList']:
            print("{}{}   {}  {}  {}  {}".format(j['cityName'],j['areaDistrict'],j['jobName'],j['salaryDesc'],j['jobLabels'],j['skills']))

            # "bossName": "于先生","bossTitle": "人力资源专员","jobName": "会计",
            # "salaryDesc": "4-5K","jobExperience": "1-3年","jobDegree": "大专","cityName": "鞍山",
            # "areaDistrict": "岫岩满族自治县","businessDistrict": "阜昌","encryptBrandId": "af8346777391596d1nNz3du6GVU~"
            # "brandScaleName": "20-99人","brandIndustry": "电子商务","brandName": "岫岩满族辉歌电子商务",
            k+=1
            # print(j)
    # break
print(k)
