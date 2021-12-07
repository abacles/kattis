#include <stdio.h>

int main()
{
  char seq[1001];
  int adj_u = 0, adj_d = 0, adj_n = 0, i;
  scanf("%s", seq);
  for (i=1; seq[i]; i++)
    {
      if (i == 1 && seq[0] != seq[1])
        {
          adj_u++;
          adj_d++;
        }
      if (seq[i] == 'D' && i > 1)
        adj_u++;
      if (seq[i] == 'D')
        adj_u++;
      if (seq[i] == 'U' && i > 1)
        adj_d++;
      if (seq[i] == 'U')
        adj_d++;
      if (seq[i] != seq[i-1])
        adj_n++;
    }
  printf("%d\n%d\n%d\n", adj_u, adj_d, adj_n);
}
