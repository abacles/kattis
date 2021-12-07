#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct edge
{
  int from, to;
  int weight;
};

int wcompar(const void *pa, const void *pb)
{
  int a = ((struct edge*)pa)->weight, b = ((struct edge*)pb)->weight;
  if(a == b)
    return 0;
  return a<b ? -1:1;
}

int lcompar(const void *pa, const void *pb)
{
  struct edge *a = (struct edge*)pa, *b = (struct edge*)pb;
  if(a->from == b->from)
    {
      if(a->to == b->to)
	return 0;
      return a->to < b->to ? -1:1;
    }
  return a->from < b->from ? -1:1;
  /*
  char sa[6], sb[6];
  if(a->from == b->from)
    {
      if(a->to == b->to)
	return 0;
      sprintf(sa, "%d", a->to);
      sprintf(sa, "%d", b->to);
      return strcmp(sa, sb) < 0 ? -1:1;
    }
  sprintf(sa, "%d", a->from);
  sprintf(sb, "%d", b->from);
  return strcmp(sa, sb) < 0 ? -1:1;
  */
}

int find(int parent[], int a)
{
  if(parent[a] != a)
    parent[a] = find(parent, parent[a]);
  return parent[a];
}

void join(int parent[], int rank[], int a, int b)
{
  a = find(parent, a);
  b = find(parent, b);
  if(rank[a] < rank[b])
    parent[a] = b;
  else
    {
      parent[b] = a;
      if(rank[a] == rank[b])
	rank[a]++;
    }
}

void kruskals(struct edge g[], int n, int m)
{
  int whichtree[20000], treerank[20000], ntrees = n, cost = 0, i;
  struct edge mst[19999];
  for(i=0;i<n;i++)
    {
      whichtree[i] = i;
      treerank[i] = 1;
    }
  qsort(g, m, sizeof(g[0]), wcompar);
  for(i=0;i<m;i++)
    {
      if(find(whichtree, g[i].to) != find(whichtree, g[i].from))
	{
	  join(whichtree, treerank, g[i].to, g[i].from);
	  cost += g[i].weight;
	  if(g[i].from < g[i].to)
	    mst[n-ntrees] = g[i];
	  else
	    {
	      mst[n-ntrees].from = g[i].to;
	      mst[n-ntrees].to = g[i].from;
	    }
	  if((--ntrees) == 1)
	    {
	      qsort(mst, n-1, sizeof(mst[0]), lcompar);
	      printf("%d\n", cost);
	      for(i=0;i<n-1;i++)
		printf("%d %d\n", mst[i].from, mst[i].to);
	      return;
	    }
	}
    }
  printf("Impossible\n");
}

int main()
{
  int n, m, i;
  struct edge graph[30000];
  while(1)
    {
      scanf("%d %d", &n, &m);
      if(!n && !m)
	break;
      for(i=0;i<m;i++)
	scanf("%d %d %d", &(graph[i].from), &(graph[i].to), &(graph[i].weight));
      kruskals(graph, n, m);
    }
}
