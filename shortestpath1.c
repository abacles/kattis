#include <stdio.h>
#include <stdlib.h>

#define INF 134217728

struct edge
{
  int in,weight;
  struct edge *next;
};

struct q
{
  int elem;
  struct q *next;
};

struct edge **graph;
int *dist;

struct edge *enew(int i,int w)
{
  struct edge *new = malloc(sizeof(struct edge));
  new->in = i,new->weight = w;
  new->next = NULL;
  return new;
}

void efree(struct edge *n)
{
  if(n->next) efree(n->next);
  free(n);
}

struct q *qnew(int e)
{
  struct q *new = malloc(sizeof(struct q));
  new->elem = e;
  new->next = NULL;
  return new;
}

void dijkstra(int s,int nc)
{
  int i,node;
  struct edge *temp;
  struct q *read,*write,*qtemp;
  for(i=0;i<nc;i++) dist[i] = INF;
  dist[s] = 0;
  read = write = qnew(s);
  while(read)
    {
      node = read->elem;
      if(read == write) write = NULL;
      qtemp = read->next,free(read),read = qtemp;
      for(temp=graph[node]->next;temp;temp=temp->next)
	{
	  if(dist[node] + temp->weight < dist[temp->in])
	    {
	      dist[temp->in] = dist[node] + temp->weight;
	      qtemp = qnew(temp->in);
	      if(write) write->next = qtemp;
	      write = qtemp;
	      if(!read) read = write;
	    }
	}
    }
}

int main()
{
  int nc,ec,qc,start,a,b,w,i;
  struct edge *temp;
  while(1)
    {
      scanf("%d %d %d %d",&nc,&ec,&qc,&start);
      if(nc+ec+qc+start == 0) break;
      graph = malloc(sizeof(struct edge*)*nc);
      dist = malloc(sizeof(int)*nc);
      for(i=0;i<nc;i++) graph[i] = enew(-1,-1);
      for(i=0;i<ec;i++)
	{
	  scanf("%d %d %d",&a,&b,&w);
	  for(temp=graph[a];temp->next;temp=temp->next);
	  temp->next = enew(b,w);
	}
      dijkstra(start,nc);
      for(i=0;i<qc;i++)
	{
	  scanf("%d",&a);
	  if(dist[a] < INF) printf("%d\n",dist[a]);
	  else printf("Impossible\n");
	}
      for(i=0;i<nc;i++) efree(graph[i]);
      free(graph);
      free(dist);
      printf("\n");
    }
}
