from concurrent.futures import ThreadPoolExecutor
from .constants import Constants
from multiprocessing import Pool, current_process

# 전역 스레드풀 초기화
# 예를 들어, 최대 스레드 개수를 7로 설정
constants = Constants.get_instance()
global_thread_pool = None
global_process_pool = None

def get_global_thread_pool() -> ThreadPoolExecutor:
    global global_thread_pool
    if global_thread_pool is None:
        global_thread_pool = ThreadPoolExecutor(max_workers=constants.ollama_file_multi_count)
    return global_thread_pool

def shutdown_global_thread_pool(wait_option:bool, cancel_futures_option:bool) -> None:
    print('[INFO] shutdown_global_thread_pool called!')
    global_thread_pool.shutdown(wait=wait_option, cancel_futures=cancel_futures_option)
    print('[INFO] shutdown_global_thread_pool completed!')

def get_global_process_pool():
    global global_process_pool
    if global_process_pool is None:
        global_process_pool = Pool(processes=constants.ollama_chunk_multi_count)
    return global_process_pool

def shutdown_global_process_pool():
    print('[INFO] shutdown_global_process_pool called!')
    global_process_pool.close()
    global_process_pool.join()
    print('[INFO] shutdown_global_process_pool completed!')

if __name__ == '__main__':
    pass