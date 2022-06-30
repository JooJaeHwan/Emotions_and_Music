import pandas as pd
import pymysql

conn = pymysql.connect(
	                    user    = '',
                        passwd  = '',
    	                port    =  000,
						db      = 'Writing',
    	                charset = 'utf8'
)

cur = conn.cursor()

cur.execute('''
SELECT DISTINCT * FROM essay AS m;
''')
result = cur.fetchall()

result = pd.DataFrame(result)
result.to_csv('./Essay.csv', index = False, header=["id", "sentences"])
# result.to_csv('./Music.csv', index = True, header=["artist_name", "song_name", "lyrics"])