#coding=utf-8
# 对抗12306多次查询后,会出现服务器繁忙问题

from auto_book import login_proc,search_proc,book_proc

result = 'gogogo'
date = '2017-01-14'
begin_time = '21:59:50'
refresh_interval = 0.1
type='T' # type = ''

for i in range(1,5):
    if result == 'gogogo':
        try:
            sel = login_proc()
            search_proc(sel,date,begin_time,type)
            result = book_proc(sel,refresh_interval)
        except:
            continue
    else:
        print result
        break
