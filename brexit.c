#include <stdio.h>
#include <stdlib.h>

struct country
{
  int *partners, npartners, pcap, ngone;
};

void init_euro(struct country euro[], int n)
{
  int i;
  for (i=0; i<n; i++)
    {
      euro[i].partners = malloc(16 * sizeof (int));
      euro[i].npartners = euro[i].ngone = 0;
      euro[i].pcap = 16;
    }
}

void add_edge(struct country euro[], int from, int to)
{
  if (euro[from].npartners == euro[from].pcap)
    euro[from].partners = realloc(euro[from].partners,
                                  (euro[from].pcap *= 2) * sizeof (int));
  euro[from].partners[euro[from].npartners++] = to;
}

int main()
{
  int n, m, x, uk, a, b, exit[200000], r, w, i;
  struct country euro[200000];
  char exited[200000] = {0};
  scanf("%d %d %d %d", &n, &m, &x, &uk);
  init_euro(euro, n);
  for (i=0; i<m; i++)
    {
      scanf("%d %d", &a, &b);
      add_edge(euro, a-1, b-1);
      add_edge(euro, b-1, a-1);
    }
  exit[0] = uk-1;
  exited[uk-1] = 1;
  r = 0, w = 1;
  while (r < w)
    {
      a = exit[r++];
      for (i=0; i<euro[a].npartners; i++)
        {
          b = euro[a].partners[i];
          euro[b].ngone++;
          if (!exited[b] && euro[b].ngone*2 >= euro[b].npartners)
            {
              exit[w++] = b;
              exited[b] = 1;
            }
        }
    }
  printf("%s\n", exited[x-1] ? "leave":"stay");
}
