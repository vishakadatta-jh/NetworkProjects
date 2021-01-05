import threading

def create_thread(list,function):
    threads = []
    
    for i in list:
        th = threading.Thread(target = function ,args = (i,))
        th.start()
        threads.append(th)
   
    for th in threads:
        th.join()