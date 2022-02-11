import time
import multiprocessing

n_cpu = multiprocessing.cpu_count()

row_num = 3200
col_num = 320

a = []
for i in range(row_num):
    a.append(range(col_num))
b = range(col_num)

def calculate_single_element(pipe, min_i, max_i):
    start_t = time.time()
    c = []
    for j in range(min_i, max_i):
        c.append(0)
        for i in range(col_num):
            c[j - min_i] += a[j][i]*b[i]
    end_t = time.time()
    pipe.send([c])
    pipe.close()
    # return c

def lambda_handler(event, context):
    if row_num >= n_cpu:
        chunk_size = int(row_num / n_cpu)
    else: chunk_size = row_num

    procs = []
    args = []
    for i in range(0, n_cpu):
        min_i = chunk_size * i
        max_i = min (chunk_size * (i+1), row_num)
        if min_i >= row_num: break
        args.append((min_i, max_i))

    
    process = []
    parent_conns = []
    for arg1, arg2 in args:
        conn1, conn2 = multiprocessing.Pipe()
        parent_conns.append(conn1)
        process.append(multiprocessing.Process(target = calculate_single_element, args= (conn2, arg1, arg2)))
    for p in process:
        p.start()
    for p in process:
        p.join()
    results = []
    for parent_conn in parent_conns:
        results.append(parent_conn.recv()[0])
    return results
    
