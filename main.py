# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    queue = [[0,i] for i in range(n)]

    for i in range(m):
        start_time, thread_index = queue.pop(0)
        output.append((thread_index, start_time))
        processing_time = data[i]
        queue.append([start_time + processing_time, thread_index])
        queue.sort()


    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
   
        # input from keyboard
        n,m = map(int, input().split()) 
        data = list(map(int, input().split()))
        result = parallel_processing(n, m, data)
        for r in result:
            print(r[0], r[1])



if __name__ == "__main__":
    main()
