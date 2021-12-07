
#include <stdio.h>
#include <stdlib.h>

#define INF 10000000

struct edge
{
  int cn;
  struct edge *next;
};

struct edge *graph[1000];
int dist[1000];

struct edge *newedge(int c)
{
  struct edge *new = malloc(sizeof(struct edge));
  new->cn = c;
  new->next = NULL;
  return new;
}

void dfs(int src)
{
  struct edge *e;
  for(e=graph[src]->next;e;e=e->next)
  {
    if(dist[e->cn] > dist[src] + 1)
    {
      dist[e->cn] = dist[src] + 1;
      dfs(e->cn);
    }
  }
}

int main()
{
  int nmovies, nhorror, ncons, horrors[1000], i, j, k;
  struct edge *tails[1000];
  scanf("%d %d %d", &nmovies, &nhorror, &ncons);
  for(i=0;i<nmovies;i++)
  {
    dist[i] = INF;
    graph[i] = tails[i] = newedge(-1);
  }
  for(i=0;i<nhorror;i++)
  {
    scanf("%d", &horrors[i]);
    dist[horrors[i]] = 0;
  }
  for(i=0;i<ncons;i++)
  {
    scanf("%d %d", &j, &k);
    tails[j] = tails[j]->next = newedge(k);
    tails[k] = tails[k]->next = newedge(j);
  }
  for(i=0;i<nhorror;i++)
    dfs(horrors[i]);
  for(i=j=0;i<nmovies;i++)
  {
    if(dist[i] > dist[j])
      j = i;
  }
  printf("%d\n", j);
}
