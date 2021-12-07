#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Ax = b

void mprint(double *A[], int n)
{
  int i, j;
  printf("[\n");
  for(i=0;i<n;i++)
    {
      for(j=0;j<n;j++)
	printf("%.2f ", A[i][j]);
      printf("| %.2f\n", A[i][n]);
    }
  printf("]\n");
}

int zero(double c)
{
  return -1e-15 <= c && c <= 1e-15;
}

void solv(double *A[], int n)
{
  int i, j, k;
  double *temp, f;
  for(i=0;i<n;i++)
    {
      for(k=i,j=i+1;j<n;j++)
        {
	  if(fabs(A[j][i]) > fabs(A[k][i]))
	    k = j;
        }
      if(zero(A[k][i]))
	{
	  for(j=0;j<n;A[j++][i]=0);
	  continue;
	}
      temp = A[k]; A[k] = A[i]; A[i] = temp;
      for(j=0;j<n;j++)
        {
	  if(i != j)
            {
	      f = zero(A[j][i]) ? 0 : A[j][i];
	      for(k=0;k<=n;k++)
		A[j][k] -= f * A[i][k] / A[i][i];
	      A[j][i] = 0;
            }
        }
    }
}

int main()
{
  int n, i, j, sol;
  double *A[100];
  for(i=0;i<100;i++)
    A[i] = malloc(sizeof(double)*101);
  while(1)
    {
      scanf("%d", &n);
      if(!n) break;
      for(i=0;i<n;i++)
        {
	  for(j=0;j<n;j++)
	    scanf("%lf", &A[i][j]);
        }
      for(i=0;i<n;i++)
	scanf("%lf", &A[i][n]);
      solv(A, n);
      sol = 1;
      for(i=0;i<n;i++)
        {
	  for(j=0; j<=n && zero(A[i][j]); j++);
	  if(j >= n)
	    sol = (j == n) ? 0 : 100;
        }
      if(sol != 1)
	printf("%s\n", (sol) ? "multiple" : "inconsistent");
      else
        {
	  for(i=0;i<n;i++)
	    printf("%f%c", A[i][n]/A[i][i], i<n-1?' ':'\n');
        }
    }
  for(i=0;i<100;free(A[i++]));
}
