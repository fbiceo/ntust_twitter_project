# -*- coding: utf-8 -*-

import pyes
import json
#建立連線
conn = pyes.es.ES('localhost:9200',default_indices='twitter2',default_types='retweet' )
#查詢全部資料
q = pyes.query.MatchAllQuery()
result = conn.search(query=q) 
#列印出資料
print json.dumps(result[0]['entities'])
