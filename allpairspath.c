#include <stdio.h>
#include <stdlib.h>

#define INF 150001

void markneg(int d[150][150], int n)
{
  int i, j, k;
  for(k=0;k<n;k++)
    {
      if(d[k][k] < 0) // this node is in a cycle
	{
	  for(i=0;i<n;i++)
	    {
	      for(j=0;j<n;j++)
		{
		  /* if a node can reach this cycle, everything past the cycle
		     that it reaches is infinitely close*/
		  if(d[i][k] != INF && d[k][j] != INF)
		    d[i][j] = -INF;
		}
	    }
	}
    }
}

void floyd_warshall(int d[150][150], int n)
{
  int i, j, k;
  for(k=0;k<n;k++)
    {
      for(i=0;i<n;i++)
	{
	  for(j=0;j<n;j++)
	    {
	      if(d[i][k] != INF && d[k][j] != INF &&
		 d[i][k] + d[k][j] < d[i][j])
		d[i][j] = d[i][k] + d[k][j];
	    }
	}
    }
  markneg(d, n);
}

int main()
{
  int n, m, nq, u, v, w, i, j;
  int dist[150][150];
  while(1)
    {
      scanf("%d %d %d", &n, &m, &nq);
      if(!n && !m && !nq)
	break;
      for(i=0;i<n;i++)
	{
	  for(j=0;j<n;j++)
	    dist[i][j] = i==j ? 0:INF;
	}
      for(i=0;i<m;i++)
	{
	  scanf("%d %d %d", &u, &v, &w);
	  if(w < dist[u][v])
	    dist[u][v] = w;
	}
      floyd_warshall(dist, n);
      for(i=0;i<nq;i++)
	{
	  scanf("%d %d", &u, &v);
	  if(dist[u][v] == INF || dist[u][v] == -INF)
	    printf("%s\n", dist[u][v]==INF ? "Impossible":"-Infinity");
	  else
	    printf("%d\n", dist[u][v]);
	}
      putchar('\n');
      /*
      for(i=0;i<n;i++)
	{
	  for(j=0;j<n;j++)
	    printf("%-8d", dist[i][j]);
	  putchar('\n');
	}
      */
    }
}
