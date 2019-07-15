import datetime


def get_cur_time():
    now = datetime.datetime.now()
    return str(now.strftime("%B%d,%Y, %H:%M:%S"))


time = get_cur_time()
print(time)
