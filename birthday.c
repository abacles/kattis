#include <stdio.h>
#include <string.h>

#define MIN(A, B) (A < B ? A:B)

int g[100][100], deg[100], pre[100], reach[100], count, bridge;

void dfs(int v, int prev)
{
  int i;
  reach[v] = pre[v] = count++;
  for (i=0; i<deg[v]; i++)
    {
      if (g[v][i] == prev) continue;
      if (pre[g[v][i]] == 0)
        {
          dfs(g[v][i], v);
          reach[v] = MIN(reach[v], reach[g[v][i]]);
          if (reach[g[v][i]] > pre[v])
            bridge = 1;
        }
      else
        reach[v] = MIN(reach[v], pre[g[v][i]]);
    }
}

int main()
{
  int n, m, i, a, b;
  while (scanf("%d %d", &n, &m), n || m)
    {
      memset(deg, 0, 100 * sizeof (int));
      memset(pre, 0, 100 * sizeof (int));
      memset(reach, 0, 100 * sizeof (int));
      for (i=0; i<m; i++)
        {
          scanf("%d %d", &a, &b);
          g[a][deg[a]++] = b;
          g[b][deg[b]++] = a;
        }
      count = 1;
      bridge = 0;
      dfs(0, -1);
      for (i=0; i<n; i++)
        if (pre[i] == 0) bridge = 1;
      printf("%s\n", bridge ? "Yes":"No");
    }
}
