#include <stdio.h>
#include <stdlib.h>

#define INF 2000000

struct edge
{
  int to, weight;
};

struct node
{
  int ne, ecap;
  struct edge *edges;
};

void init_graph(struct node all[], int n)
{
  int i;
  for(i=0;i<n;i++)
    {
      all[i].ne = 0;
      all[i].ecap = 1;
      all[i].edges = malloc(sizeof(struct edge));
    }
}

void free_graph(struct node all[], int n)
{
  int i;
  for(i=0;i<n;i++)
    free(all[i].edges);
}

void add_edge(struct node all[], int u, int v, int w)
{
  if(all[u].ne == all[u].ecap)
    {
      all[u].ecap *= 2;
      all[u].edges = realloc(all[u].edges, sizeof(struct edge)*all[u].ecap);
    }
  (all[u].edges[all[u].ne]).to = v;
  (all[u].edges[all[u].ne]).weight = w;
  (all[u].ne)++;
}

int relax_all(struct node g[], int n, int dist[], int prev[], char neg[])
{
  int i, j, change = 0;
  for(i=0;i<n;i++)
    {
      if(dist[i] == INF)
	continue;
      for(j=0;j<g[i].ne;j++)
	{
	  if(dist[i] + (g[i].edges[j]).weight < dist[(g[i].edges[j]).to])
	    {
	      dist[(g[i].edges[j]).to] = dist[i] + (g[i].edges[j]).weight;
	      prev[(g[i].edges[j]).to] = i;
	      if(neg)
		neg[(g[i].edges[j]).to] = 1;
	      change = 1;
	    }
	}
    }
  return change;
}

void markneg(struct node g[], char neg[], int dist[], int prev[], int n)
{
  int q[1000], qr = 0, qw = 0, i, j, v;
  for(i=0;i<n;i++)
    {
      if(neg[i])
	{
	  for(v=i,j=0;j<n;j++)
	    v = prev[v];
	  neg[i] = 0;
	  neg[v] = 1;
	}
    }
  for(i=0;i<n;i++)
    {
      if(neg[i])
	{
	  q[qw++] = i;
	  dist[i] = -INF;
	}
    }
  while(qr < qw)
    {
      v = q[qr++];
      for(i=0;i<g[v].ne;i++)
	{
	  if(dist[(g[v].edges[i]).to] != -INF)
	    {
	      q[qw++] = (g[v].edges[i]).to;
	      dist[(g[v].edges[i]).to] = -INF;
	    }
	}
    }
}

int *bellman_ford(struct node g[], int n, int src)
{
  int *dist = malloc(sizeof(int)*n);
  int prev[1000], i;
  char neg[1000] = {0};
  for(i=0;i<n;i++)
    {
      dist[i] = INF;
      prev[i] = i;
    }
  dist[src] = 0LL;
  for(i=0;i<n-1;i++)
    {
      if(!relax_all(g, n, dist, prev, NULL))
	return dist;
    }
  if(relax_all(g, n, dist, prev, neg))
    markneg(g, neg, dist, prev, n);
  return dist;
}

int main()
{
  int n, m, s, nq, u, v, w, i;
  int *dist;
  struct node graph[1000];
  while(1)
    {
      scanf("%d %d %d %d", &n, &m, &nq, &s);
      if(!n && !m && !nq && !s)
	break;
      init_graph(graph, n);
      for(i=0;i<m;i++)
	{
	  scanf("%d %d %d", &u, &v, &w);
	  add_edge(graph, u, v, w);
	}
      dist = bellman_ford(graph, n, s);
      for(i=0;i<nq;i++)
	{
	  scanf("%d", &u);
	  if(dist[u] == INF || dist[u] == -INF)
	    printf("%s\n", dist[u]==INF ? "Impossible":"-Infinity");
	  else
	    printf("%d\n", dist[u]);
	}
      free_graph(graph, n);
      free(dist);
    }
}
