#include <stdio.h>
#include <stdlib.h>

struct edge
{
  int cn;
  struct edge *next;
} *graph[200000];

char visited[200000] = {0};

struct edge *newedge(int c)
{
  struct edge *new = malloc(sizeof(struct edge));
  new->cn = c;
  new->next = NULL;
  return new;
}

void fredge(struct edge *e)
{
  if(e->next)
    fredge(e->next);
  free(e);
}

void dfs(int n)
{
  struct edge *e;
  visited[n] = 1;
  for(e=graph[n]->next;e;e=e->next)
    {
      if(!visited[e->cn])
	dfs(e->cn);
    }
}

int main()
{
  struct edge *tails[200000];
  int nhouses, ncables, i, a, b, t = 1;
  scanf("%d %d", &nhouses, &ncables);
  for(i=0;i<nhouses;i++)
    tails[i] = graph[i] = newedge(-1);
  for(i=0;i<ncables;i++)
    {
      scanf("%d %d", &a, &b);
      tails[a-1] = tails[a-1]->next = newedge(b-1);
      tails[b-1] = tails[b-1]->next = newedge(a-1);
    }
  dfs(0);
  for(i=0;i<nhouses;i++)
    {
      if(!visited[i])
	{
	  printf("%d\n", i + 1);
	  t = 0;
	}
      fredge(graph[i]);
    }
  if(t)
    printf("Connected\n");
}
