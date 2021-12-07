#include <stdio.h>

int main()
{
  char s[1000001], ch;
  int i = 0;
  while((ch = getchar()) != EOF && ch != '\n')
    {
      if (ch == '<')
        i--;
      else
        s[i++] = ch;
    }
  s[i] = '\0';
  printf("%s\n", s);
}
