# encoding=utf8
import os
import time
import logging

logging.basicConfig(level=logging.INFO, filename='ping_info.txt')
log = logging.getLogger(__name__)

success_count = 0
failed_count = 0
tot_count = 0


def main():
    global success_count, failed_count, tot_count
    tot_count += 1
    data = os.popen('ping  baidu.com').read()
    time.sleep(5)
    if '(0% 丢失)' in data:
        success_count += 1
        log.info('ping pass times {}/{}, pass rate:{:2}%'.
                 format(success_count, tot_count, int((success_count / tot_count) * 100)))
    else:
        failed_count += 1
        log.error('ping fail times{}/{}, fail rate:{:2}%'.
                  format(failed_count, tot_count, int((failed_count / tot_count) * 100)))

    os.popen('\033')


if __name__ == '__main__':
    try:
        print('Running and save log')
        while True:
            main()
    except KeyboardInterrupt:
        raise Exception('Abort by user')