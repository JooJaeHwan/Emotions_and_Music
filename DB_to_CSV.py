import pandas as pd
import pymysql

conn = pymysql.connect(
	                    user    = '',
                        passwd  = '',
    	                port    =  0000,
    	                charset = 'utf8'
)

cur = conn.cursor()

cur.execute('''
SELECT DISTINCT * FROM Music.music AS m 
''')
result = cur.fetchall()

result = pd.DataFrame(result)
# result.to_csv('./Data.csv', index = True, header=["sentences"])
result.to_csv('./Music.csv', index = True, header=["artist_name", "song_name", "lyrics"]) 