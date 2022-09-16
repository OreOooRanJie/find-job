def consumer():
    print("consumer----------")
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[消费者]Consuming %s...' % n)
        r = '200 OK'

def producer(c):
    print("producer----------")
    # 启动生成器
    c.send(1)
    # next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('[生产者]Producing %s...' % n)
        r = c.send(n)
        print('[生产者]Consumer return: %s' % r)
    c.close()

if __name__ == '__main__':
    c = consumer()
    producer(c)