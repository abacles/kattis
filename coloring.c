#include <stdio.h>

#define MIN(A, B) (A < B ? A:B)

int g[11][11], deg[11] = {0}, coloring[11], n, chi = 11;

void chroma(int v, int k)
{
  int palette[11] = {0}, i;
  if (v >= n) 
    {
      chi = MIN(chi, k);
      return;
    }
  for (i=0; i<deg[v]; i++)
    if (g[v][i] < v)
      palette[coloring[g[v][i]]] = 1;
  for (i=0; i<k; i++)
    if (!palette[i])
      {
        coloring[v] = i;
        chroma(v+1, k);
      }
  coloring[v] = k;
  chroma(v+1, k+1);
}

int main()
{
  int i;
  char delim;
  scanf("%d", &n);
  for (i=0; i<n; i++)
    while (scanf("%d%c", &g[i][deg[i]++], &delim), delim != '\n');
  coloring[0] = 0;
  chroma(1, 1);
  printf("%d\n", chi);
}
