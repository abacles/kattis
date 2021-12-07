#include <stdio.h>

int main()
{
  int n, i, j, k, space, pos = 0;
  char d[200001];
  scanf("%d", &n);
  scanf("%s", d);
  for (i=0; i<n-1; )
    {
      if (i > 0 && d[i] == 'L')
        {
          printf("%d\n", space--);
          i++;
        }
      else
        {
          space = pos;
          for (k=0; i < n-1 && d[i] != 'L'; i++, k++);
          for (j=i; j < n-1 && d[j] == 'L'; j++);
          pos += 1 + j-i;
          for (j=0; j<k ;j++)
            printf("%d\n", pos++);
        }
    }
}
