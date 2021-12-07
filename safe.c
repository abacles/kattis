#include <stdio.h>

int zip(int config[9])
{
  int z = 0, i;
  for (i=0; i<9; i++)
    z = (4 * z) + config[i];
  return z;
}

void unzip(int config[9], int z)
{
  int i;
  for (i=8; i>=0; i--, z/=4)
    config[i] = z % 4;
}

int bfs(int start)
{
  int q[300000], dist[300000], config[9], newconf[9], qr = 0, qw = 0, v, w, i, j;
  for (i=0; i<300000; i++)
    dist[i] = -1;
  dist[start] = 0;
  q[qw++] = start;
  while (qr < qw)
    {
      unzip(config, v = q[qr++]);
      for (i=0; i<9; i++)
        {
          for (j=0; j<9; j++)
            newconf[j] = (config[j] + (j/3 == i/3 || j%3 == i%3)) % 4;
          w = zip(newconf);
          if (dist[w] == -1)
            {
              dist[w] = dist[v] + 1;
              q[qw++] = w;
              if (w == 0) return dist[w];
            }
        }
    }
  return -1;
}

int main()
{
  int safe[9], i;
  for (i=0; i<9; scanf("%d", &safe[i++]));
  printf("%d\n", bfs(zip(safe)));
}
