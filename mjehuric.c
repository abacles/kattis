#include <stdio.h>

void swap(int a[], int i, int j)
{
  int temp = a[i];
  a[i] = a[j];
  a[j] = temp;
  for (i=0; i<5; i++)
    printf("%d%c", a[i], i<4?' ':'\n');
}

int main()
{
  int a[5], i, k;
  for (i=0; i<5; i++)
    scanf("%d", &a[i]);
  while (1)
    {
      for (k=i=0; i<4; i++)
        {
          if (a[i] > a[i+1])
            {
              swap(a, i, i+1);
              k = 1;
            }
        }
      if (!k) break;
    }
}
