#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MIN(A, B) ((A)<(B) ? (A):(B))

double dist(int x1, int y1, int x2, int y2)
{
  return hypot(x1 - x2, y1 - y2);
}

int main()
{
  int x, y, x1, y1, x2, y2;
  scanf("%d %d %d %d %d %d", &x, &y, &x1, &y1, &x2, &y2);
  if (x1 <= x && x <= x2)
    printf("%d\n", MIN(abs(y - y1), abs(y - y2)));
  else if (y1 <= y && y <= y2)
    printf("%d\n", MIN(abs(x - x1), abs(x - x2)));
  else
    printf("%f\n", MIN(MIN(dist(x, y, x1, y1), dist(x, y, x2, y2)),
                       MIN(dist(x, y, x1, y2), dist(x, y, x2, y1))));
}
