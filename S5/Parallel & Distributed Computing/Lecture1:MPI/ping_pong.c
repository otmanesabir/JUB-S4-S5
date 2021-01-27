#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(NULL, NULL);
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    if (world_rank==0)
    {
        int value_to_be_sent = 41; int dest = 1;
        MPI_Send(&value_to_be_sent, 1, MPI_INTEGER, dest, 0, MPI_COMM_WORLD);

        int source = dest; int received_value=0;
        MPI_Recv(&received_value, 1, MPI_INTEGER, source, 0, MPI_COMM_WORLD, NULL);

        printf("The received answer is %d\n", received_value);
    }
    else if (world_rank==1)
    {
        int received_value = 0; int source = 0;
        MPI_Recv(&received_value, 1, MPI_INTEGER, source, 0, MPI_COMM_WORLD, NULL);

        int new_value = received_value+1;
        int dest = source;
        MPI_Send(&new_value, 1, MPI_INTEGER, dest, 0, MPI_COMM_WORLD);        
    }

    MPI_Finalize();
}
