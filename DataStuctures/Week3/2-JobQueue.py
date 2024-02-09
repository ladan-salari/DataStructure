# python3

from collections import namedtuple
import math
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def LeftChild(index):
    return 2*index + 1

def RightChild(index):
    return 2*index + 2

def SiftDown(index, n_workers, next_free_time):
    minindex = index
    l = LeftChild(index)
    r = RightChild(index)

    if l < n_workers and CompareWorker(next_free_time[l], next_free_time[minindex]):
        minindex = l

    if r < n_workers and CompareWorker(next_free_time[r], next_free_time[minindex]):
        minindex = r
    if index != minindex:
        next_free_time[index], next_free_time[minindex] = next_free_time[minindex], next_free_time[index]
        SiftDown(minindex, n_workers, next_free_time)

def CompareWorker(worker1, worker2):
    if worker1[1] != worker2[1]:
        return worker1[1] < worker2[1]
    else:
        return worker1[0] < worker2[0]

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    assign_workers = [None] * len(jobs)
    next_free_time = [[i, 0] for i in range(n_workers)]
    start_time = [None] *len(jobs)
    for i in range(len(jobs)):
        assign_workers[i] = next_free_time[0][0]
        start_time[i] = next_free_time[0][1]
        next_free_time[0][1] += jobs[i]
        SiftDown(0, n_workers, next_free_time)
        # next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        # result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        # next_free_time[next_worker] += job
    return assign_workers, start_time

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assign_workers, start_time = assign_jobs(n_workers, jobs)

    for i in range(len(jobs)):
        print(assign_workers[i], start_time[i])


if __name__ == "__main__":
    main()
