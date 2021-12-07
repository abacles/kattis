#include <stdio.h>
#include <stdlib.h>

#define INF 0x7FFFFFFF

struct dian
{
  int *v, *w;
  int nv, cap;
} net[180001];

int inmap(int maxr, int maxc, int r, int c)
{
  return 0 <= r && r < maxr && 0 <= c && c < maxc;
}

void add_edge(int from, int to, int weight)
{
  if(net[from].nv == net[from].cap)
    {
      net[from].v = realloc(net[from].v, sizeof(int)*(net[from].cap*=2));
      net[from].w = realloc(net[from].w, sizeof(int)*(net[from].cap));
    }
  net[from].v[net[from].nv] = to;
  net[from].w[(net[from].nv)++] = weight;
}

void augment_edge(int from, int to, int weight)
{
  int i;
  for(i=0; i<net[from].nv && net[from].v[i]!=to; i++);
  if(net[from].v[i] != to)
    add_edge(from, to, weight);
  else if(net[from].w[i] != INF)
    net[from].w[i] += weight;
}

int get_flow(int from, int to)
{
  int i;
  for(i=0;net[from].v[i]!=to;i++);
  return net[from].w[i];
}

int mincut(int sink, int n)
{
  int mf = 0, cf, prev[180001], q[180001], qw, qr, u, i, t;
  while(1)
    {
      for(i=0;i<n;i++)
        prev[i] = -1;
      qw = qr = 0;
      q[qw++] = n;
      prev[n] = -2;
      while(qr < qw)
	{
	  u = q[qr++];
	  for(i=0;i<net[u].nv;i++)
	    {
	      if(prev[net[u].v[i]] == -1 && net[u].w[i] > 0)
		{
		  q[qw++] = net[u].v[i];
		  prev[net[u].v[i]] = u;
		}
	    }
	  if(prev[sink] != -1)
	    break;
	}
      if(prev[sink] == -1)
	return mf;
      for(u=sink,cf=INF;prev[u]>=0;u=prev[u])
	{
	  if((t=get_flow(prev[u], u)) < cf)
	    cf = t;
	}
      for(u=sink;prev[u]>=0;u=prev[u])
	{
	  augment_edge(prev[u], u, -cf);
	  augment_edge(u, prev[u], cf);
	}
      mf += cf;
    }
}

int main()
{
  int r, c, cc, cr, i, j, d;
  scanf("%d %d", &r, &c);
  for(i=0;i<2*r*c+1;i++)
    {
      net[i].nv = 0, net[i].cap = 1;
      net[i].v = malloc(sizeof(int)*4), net[i].w = malloc(sizeof(int)*4);
    }
  for(i=0;i<r;i++)
    {
      for(j=0;j<c;j++)
	{
	  scanf("%d", &d);
	  add_edge(i*c+j, r*c+i*c+j, d);
	  for(d=-1;d<=1;d+=2)
	    {
	      if(inmap(r, c, i+d, j))
		add_edge(r*c+i*c+j, (i+d)*c+j, INF);
	      if(inmap(r, c, i, j+d))
		add_edge(r*c+i*c+j, i*c+j+d, INF);
	    }
	  if(!i || !j || i==r-1 || j==c-1)
	    add_edge(2*r*c, i*c+j, INF); // add backward edge?
	}
    }
  scanf("%d %d", &cr, &cc);
  printf("%d\n", mincut(r*c+cr*c+cc, 2*r*c));
  for(i=0;i<2*r*c+1;i++)
    free(net[i].v), free(net[i].w);
}
