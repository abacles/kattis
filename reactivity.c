#include <stdio.h>
#include <stdlib.h>

struct edge
{
  int to;
  struct edge *next;
} *graph[1000], *tails[1000];

struct edge *nedge(int c)
{
  struct edge *new = malloc(sizeof(struct edge));
  new->to = c, new->next = NULL;
  return new;
}

void fedge(struct edge *e)
{
  if(e->next)
    fedge(e->next);
  free(e);
}

int main()
{
  int nelems, nedges, bef[1000] = {0}, ord[1000], done[1000] = {0}, a, b, i, j, f;
  struct edge *t;
  scanf("%d %d", &nelems, &nedges);
  for(i=0;i<nelems;i++)
    tails[i] = graph[i] = nedge(-1);
  for(i=0;i<nedges;i++)
    {
      scanf("%d %d", &a, &b);
      tails[a] = tails[a]->next = nedge(b);
      bef[b]++;
    }
  for(i=0;i<nelems;i++)
    {
      for(f=-1,j=0;j<nelems;j++)
	{
	  if(!done[j] && !bef[j] && f == -1)
	    f = j;
	  else if(!done[j] && !bef[j] && f != -1)
	    break;
	}
      if((f != -1 && j < nelems) || f == -1)
	break;
      ord[i] = f;
      done[f] = 1;
      for(t=graph[f]->next;t;t=t->next)
	bef[t->to]--;
    }
  if(i < nelems)
    printf("back to the lab\n");
  else
    {
      for(i=0;i<nelems;i++)
	printf("%d%c", ord[i], i!=nelems-1?' ':'\n');
    }
  for(i=0;i<nelems;i++)
    fedge(graph[i]);
}
