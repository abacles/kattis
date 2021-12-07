#include <stdio.h>
#include <stdlib.h>

int find(int p[], int a)
{
  if(p[a] != a)
    return p[a] = find(p, p[a]);
  return a;
}

void join(int p[], int rank[], int a, int b)
{
  a = find(p, a);
  b = find(p, b);
  if(rank[a] < rank[b])
    p[a] = b;
  else
    {
      p[b] = a;
      if(rank[a] == rank[b])
	(rank[a])++;
    }
}

int main()
{
  int n, q, *parent, *rank, a, b, i;
  char op, foo;
  scanf("%d %d", &n, &q);
  parent = malloc(sizeof(int) * n);
  rank = malloc(sizeof(int) * n);
  for(i=0;i<n;i++)
    {
      parent[i] = i;
      rank[i] = 1;
    }
  for(i=0;i<q;i++)
    {
      scanf("%c%c %d %d", &foo, &op, &a, &b);
      if(op == '?')
	printf("%s\n", (find(parent, a) == find(parent, b) ? "yes" : "no"));
      else
	join(parent, rank, a, b);
    }
  free(parent);
  free(rank);
}
