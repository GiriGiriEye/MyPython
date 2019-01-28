import time

def _getCurrentTime():
    currentTime = time.strftime('%Y') + '年' + time.strftime('%m') + '月' + time.strftime(
        '%d') + '日' + ' ' + time.strftime('%H') + '时' + time.strftime('%M') + '分' + time.strftime('%S') + '秒'

    return currentTime