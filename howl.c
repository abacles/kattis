#include <stdio.h>

int main()
{
  int len, ch, i;
  while (ch = getchar(), 'A' <= ch && ch <= 'Z')
    len++;
  for (i=0; i<len; i++)
    putchar('A');
  printf("WHO\n");
}
