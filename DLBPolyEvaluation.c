#include<stdio.h>
#include<stdlib.h>
#include<mpi.h>

#define MAX 50003
//#define MAX 100
#define COEFFICIENT 1
#define TERM 10

// Use Pascal server for this assignment. Use Everest only when you can not access Pascal.
// mpicc DLBPolyEvaluation.c
// mpirun -np 3 ./a.out

// Two tags to distinguish work messages from process-termination messages
#define WORKTAG 1
#define DIETAG 2

double power(double x, int degree)
{     
      if(degree == 0)  return 1;
      
      if(degree == 1)  return x;

      return x * power(x, degree - 1);
}

// to be called from worker process
double evaluateTerm(int coefficient, int degree, double x)
{
      double powerX = power(x, degree);

      double answer = answer + coefficient * powerX;
      
      return answer;
}

double sequential(int coeffArr[], double x)
{
   int i;
   double  answer = 0;
   
   // updated the stopping value of loop to MAX-1 
   for( i = 0; i < MAX;  i++)
   {
      double powerX = power(x, i);

      //printf("%f ", powerX);
      answer = answer + coeffArr[i] * powerX;
   }
   return answer;
}

void initialize(int coeffArr[])
{
   int i;
   for( i = 0; i < MAX; i++)
   {
      coeffArr[i] = COEFFICIENT;
   }
}

void master(int coeffArr[], int numTerms)
{
      int numProcs;
	  MPI_Comm_size(MPI_COMM_WORLD, &numProcs); 
	
	  MPI_Status status;
	
	  // MPI_Send(const void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm)
      int tCount = 0;
      int workerRank;
      int term[2];
      
      for(workerRank = 1; workerRank < numProcs; workerRank++)
      {   
         term[0] = tCount;  // degree
         term[1] = coeffArr[tCount];  // coefficient

         MPI_Send(term, TERM, MPI_INT, workerRank, WORKTAG, MPI_COMM_WORLD); 
         tCount++;
      }
      // receive the work done by workers
      double termAnswer;
      double finalAnswer = 0;
      
      while(tCount < MAX)
      {    
          // Receive the results from workers and accumulate the result
          MPI_Recv(&termAnswer, 1, MPI_DOUBLE, MPI_ANY_SOURCE, WORKTAG, MPI_COMM_WORLD, &status);
          finalAnswer = finalAnswer + termAnswer;
          workerRank = status.MPI_SOURCE;

          term[0] = tCount;  // degree
          term[1] = coeffArr[tCount];  // coefficient
          MPI_Send(term, TERM, MPI_INT, workerRank, WORKTAG, MPI_COMM_WORLD); 
          
          tCount++;
      }
      	
      // Send (tag = DIETAG) to all workers
      for(workerRank = 1; workerRank < numProcs; workerRank++)
      {
        // sending garbage value because it will be ignored at worker
        term[0] = -111;  term[1] = -111;
        MPI_Send(term, TERM, MPI_INT, workerRank, DIETAG, MPI_COMM_WORLD); 
      }
     
      // Do pending receives for outstanding messages from workers
      for(workerRank = 1; workerRank < numProcs; workerRank++)
      {
        MPI_Recv(&termAnswer, 1, MPI_DOUBLE, workerRank, WORKTAG, MPI_COMM_WORLD, &status);
        finalAnswer = finalAnswer + termAnswer;
      }
      printf("Master summed up to %f", finalAnswer);
      fflush(stdout);
     // MPI_Recv(void *buf, int count, MPI_Datatype datatype, int source, int tag, MPI_Comm comm, MPI_Status *status)
}
  
void worker(double x)
{
	MPI_Status status;
    int val; 
        
    // worker keeps looping; waiting for work items from master process, 
    // unless it gets termination message
    while(1)
    { 
       int term[2];
       MPI_Recv(term, TERM, MPI_INT, 0, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
       
       if(status.MPI_TAG == DIETAG)
       {
           //printf("TERMINATING. BYE \n");
           fflush(stdout);
           return;
       }
       else    // (status.MPI_TAG = WORKTAG)
       {
         // evaluateTerm(int coefficient, int degree, double x)
         double answer = evaluateTerm(term[1], term[0], x);
         MPI_Send(&answer, 1, MPI_DOUBLE, 0, WORKTAG, MPI_COMM_WORLD);
         //printf(" degree %d coeff %d value %0.12f \n", term[0], term[1], answer);
         fflush(stdout);
       }
    } 
}

int main1()
{
    int *coeffArr = (int *)malloc(sizeof(int) * MAX);
    double x = 0.99;
    //double x = 1.000000000001;
    
    initialize(coeffArr);
    double value = sequential(coeffArr, x);
    printf(" sequential value %f \n", value);
    free(coeffArr);
    
    return 0;
} 

// Driver Code
int main(int argc, char **argv)
{ 
    int *coeffArr = (int *)malloc(sizeof(int) * MAX);
    double x = 0.99;
    //double x = 1.000000000001;
    
    initialize(coeffArr);
    
    MPI_Init(&argc, &argv);
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        
    if (rank == 0) 
    {
       master(coeffArr, MAX);
    } 
    else 
    {
       worker(x);
    }
    
    free(coeffArr);
    
    MPI_Finalize();
    
	return 0;
}

/*
    sequential code measurement

    // Start timer
    double elapsed_time = - MPI_Wtime();
    
    double value = sequential(coeffArr, x);
    
    // End timer 
    elapsed_time = elapsed_time + MPI_Wtime();
    
    printf(" sequential value %f wall clock time %8.6f \n", value, elapsed_time);
    fflush(stdout);

*/
