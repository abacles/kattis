#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int bc,mc,(*beacons)[2],(*mountains)[3];
char *visited;

int block(int b1[2],int b2[2],int m[3])
{
  float k,dist;
  // if(b2[0] == b1[0]) dist = 
  k = 1.0 * (b2[1]-b1[1]) / (b2[0]-b1[0]);
  dist = fabsf(k * m[0] - m[1] + b1[1]-k*b1[0]) / sqrt(k*k+1);
  return dist < m[2];
}

int reach(int a,int b)
{
  int i;
  for(i=0;i<mc;i++)
    if(block(beacons[a],beacons[b],mountains[i])) return 0;
  return 1;
}

void explore(int node)
{
  int i,j;
  visited[node] = 1;
  for(i=node+1;i<bc;i++)
    {
      if(!visited[i] && reach(node,i))
	explore(i);
    }
}

int main()
{
  int i,j,k,r,ccc = 0;
  scanf("%d %d",&bc,&mc);
  beacons = malloc(sizeof(int)*2*bc);
  mountains = malloc(sizeof(int)*3*mc);
  visited = malloc(sizeof(char)*bc);
  for(i=0;i<bc;i++)
    scanf("%d %d",&beacons[i][0],&beacons[i][1]);
  for(i=0;i<mc;i++)
    scanf("%d %d %d",&mountains[i][0],&mountains[i][1],&mountains[i][2]);
  for(i=0;i<bc;i++) visited[i] = 0;
  for(i=0;i<bc;i++)
    {
      if(!visited[i])
	{
	  ccc++;
	  explore(i);
	}
    }
  printf("%d\n",ccc-1);
  free(beacons);
  free(mountains);
  free(visited);
}
