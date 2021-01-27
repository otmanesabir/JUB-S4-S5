#include <stdio.h>  // like import ...
#include <stdlib.h>
#include <sys/time.h>

int main(int argc, char** argv)  // def main(argc, argv):
{   
	int N = 16*1024;
	int M = 16*1024;

	double* x = malloc(N*sizeof(double)); // allocate vectors of
	double* y = malloc(M*sizeof(double)); // size N
	double* A = malloc(M*N*sizeof(double)); // allocate vector of size MxN
	// fill x with random values
	for (int j = 0; j<N; j++) // for j in range(N):
	{
		x[j] = (double)rand()/((double)RAND_MAX);  // x[i] = random.random()
	}

	// fill y with zeros
	for (int i = 0; i<M; i++) // for i in range(M):
	{
		y[i] = 0.0;
	}

	// fill A with random values
	for (int i = 0; i<M; i++) // for i in range(M):
	{
		for (int j = 0; j<N; j++) // for j in range(N):
		{
			A[i*N+j] = (double)rand()/((double)RAND_MAX);  // A[i][j] = random.random()
		}
	}
    
	// measuring time before matrix vector product
	struct timeval t1;
	gettimeofday(&t1, NULL);

	// execute matrix vector product
	#pragma omp parallel for
	for (int i = 0; i<M; i++) // for i in range(M):
	{
		y[i] = 0.0;
		for (int j = 0; j<N; j++)  // for j in range(N):
		{
			y[i] = y[i] + A[i*N+j]*x[j];
		}
	}

	// measuring time after matrix vector product
	struct timeval t2;
	gettimeofday(&t2, NULL);

	// compute time difference in seconds as elapsed time during MVP
	double elapsed_time = ((double)t2.tv_sec + (double)t2.tv_usec * 1.0e-6) - ((double)t1.tv_sec + (double)t1.tv_usec * 1.0e-6);

	printf("The matrix vector product was computed in %lf seconds\n", elapsed_time);

	free(x); free(y); free(A); // delete allocated memory
}
