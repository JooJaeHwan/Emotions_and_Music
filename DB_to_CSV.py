import pandas as pd
import pymysql

conn = pymysql.connect(
	                    user    = '',
                        passwd  = '',
    	                port    = 0000,
						db      = 'Music',
    	                charset = 'utf8'
)

cur = conn.cursor()

cur.execute('''
SELECT DISTINCT m.artist_name, m.song_name, m.lyrics FROM music AS m;
''')
result = cur.fetchall()

result = pd.DataFrame(result)
# result.to_csv('./Writing.csv', index = True, header=["sentences"])
result.to_csv('./Music.csv', index = True, header=["artist_name", "song_name", "lyrics"])