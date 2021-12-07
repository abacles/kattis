#include <stdio.h>

int main()
{
  char cards[51], i, j;
  scanf("%s", cards);
  for (i=0; cards[i]; i++)
    for (j=i+1; cards[j]; j++)
      if (cards[i] == cards[j])
        {
          printf("0\n");
          return 0;
        }
  printf("1\n");
}
