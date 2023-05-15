import mylib
import dbdb

#멜론가져오기
m_list = mylib.melon()
print(m_list)
#멜론에서 가져온 데이터리스트를 db에 넣기
dbdb.save_data(m_list)