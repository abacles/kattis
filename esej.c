#include <stdio.h>

void nextword(char s[])
{
  int i;
  for (i=0; s[i]; i++)
    {
      if (++s[i] <= 'z')
        return;
      s[i] = 'a';
    }
  s[i] = 'a';
  s[i+1] = '\0';
}

int main()
{
  int a, b, i;
  char word[16] = "a";
  scanf("%d %d", &a, &b);
  for (i=0; i<b; i++)
    {
      printf("%s%c", word, i<b-1?' ':'\n');
      nextword(word);
    }
}
