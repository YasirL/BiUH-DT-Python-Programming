from multiprocessing import Process
import time

def child_task():
    print("Child running")
    time.sleep(3)  # 子进程模拟耗时操作
    print("Child finished")

if __name__ == '__main__':
    p = Process(target=child_task)
    p.start()
    # 没有 join，主进程直接执行后续代码
    #p.join()
    print("Parent Stopped")