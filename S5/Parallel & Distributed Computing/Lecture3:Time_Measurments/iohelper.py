from mpi4py import MPI
import random as rnd
import csv

def fill_random_vec(M, comm):
    local_M = int(M / comm.Get_size())
    x = [rnd.random() for _ in range(local_M)]
    return x,M

def fill_random_mat(M, N, comm):
    local_M = int(M / comm.Get_size())
    x = [rnd.random() for _ in range(local_M*N)]
    return x,M,N
    

def read_vec_from_file(file_name, comm):
    M = sum(1 for line in open(file_name))
    local_M = int(M / comm.Get_size())
    rank = comm.Get_rank()
    
    x = [0.0] * local_M

    with open(file_name, 'r') as f:
        for _ in range(local_M*rank):
            next(f)
        i = 0
        for row in csv.reader(f, delimiter=','):
            x[i]=float(row[0])
            i = i + 1
            if i>=local_M:
                break

    return x,M

def read_mat_from_file(file_name, comm):
    M = sum(1 for line in open(file_name))
    local_M = int(M / comm.Get_size())
    rank = comm.Get_rank()

    for row in csv.reader(open(file_name,'r'), delimiter=','):
        N = len(row)
        break

    A = [0.0] * local_M * N

    with open(file_name, 'r') as f:
        for _ in range(local_M*rank):
            next(f)
        i = 0
        for row in csv.reader(f, delimiter=','):
            for j in range(N):
                A[i*N+j]=float(row[j])
            i = i + 1
            if i>=local_M:
                break

    return A,M,N

def print_vec(x, M, comm):
    local_M = int(M / comm.Get_size())
    rank = comm.Get_rank()

    for r in range(comm.Get_size()):
        if r == rank:
            for i in range(local_M):
                print(rank*local_M+i,x[i])
    

def print_mat(A, M, N, comm):
    local_M = int(M / comm.Get_size())
    rank = comm.Get_rank()

    print(M, local_M, N)

    for r in range(comm.Get_size()):
        if r == rank:
            for i in range(local_M):
                out_string = str(rank*local_M+i) + "  "
                for j in range(N):
                     out_string = out_string + str(A[i*N+j]) + '\t'
                print(out_string)


