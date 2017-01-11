from multiprocessing import Process, Queue
sentinel = -1


def creator(data, q):
    print("creating data and putting it in Queue")
    for item in data:
        q.put(item)


def my_consumer(q):
    while True:
        data = q.get()
        if data is sentinel:
            break
        print("data found to be processed: {}".format(data))
        processed = data * 2
        print(processed)

if __name__ == "__main__":
    q = Queue()
    data = [i * 5 for i in xrange(1, 6)] + [-1]
    process_one = Process(target=creator, args=(data, q))
    process_two = Process(target=my_consumer, args=(q,))
    process_one.start()
    process_two.start()
    q.close()
    q.join_thread()
    process_one.join()
    process_two.join()
