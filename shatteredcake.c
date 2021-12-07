#include <stdio.h>

int main()
{
  int width, npieces, i, w, l;
  long long area = 0;
  scanf("%d %d", &width, &npieces);
  for(i=0;i<npieces;i++)
    {
      scanf("%d %d", &w, &l);
      area += w * l;
    }
  printf("%lld\n", area / width);
}
