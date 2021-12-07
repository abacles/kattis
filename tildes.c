#include <stdio.h>
#include <stdlib.h>

int parent[1000000], rank[1000000], size[1000000];

int find(int x)
{
  if (parent[x] != x)
    parent[x] = find(parent[x]);
  return parent[x];
}

void merge(int x, int y)
{
  x = find(x);
  y = find(y);
  if (x == y) return;
  if (rank[x] < rank[y])
    {
      parent[x] = y;
      size[y] += size[x];
    }
  else
    {
      parent[y] = x;
      size[x] += size[y];
      if (rank[x] == rank[y])
        rank[x]++;
    }
}

int main()
{
  int n, q, a, b, i;
  char op;
  scanf("%d %d", &n, &q);
  for (i=0; i<n; i++)
    {
      parent[i] = i;
      rank[i] = size[i] = 1;
    }
  for (i=0; i<q; i++)
    {
      getchar();
      op = getchar();
      if (op == 't')
        {
          scanf("%d %d", &a, &b);
          merge(a-1, b-1);
        }
      else
        {
          scanf("%d", &a);
          printf("%d\n", size[find(a-1)]);
        }
    }
}
