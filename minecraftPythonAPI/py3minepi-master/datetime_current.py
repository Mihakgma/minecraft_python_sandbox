from datetime import datetime


def get_current_time():
    current_time_stamp = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    return current_time_stamp


if __name__ == '__main__':
    print(get_current_time())
