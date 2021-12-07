#include <stdio.h>
#include <string.h>

void flip(char from[], char to[], int len)
{
  int i;
  for (i=0; i<len; i++)
    to[i] = from[len-1-i];
}

int main()
{
  char s[51], current[51], smallest[51] = "~", len, i, j;
  scanf("%s", s);
  len = strlen(s);
  for (i=1; i<len-1; i++)
    {
      flip(s, current, i);
      for (j=i+1; j<len; j++)
        {
          flip(&s[i], &current[i], j-i);
          flip(&s[j], &current[j], len-j);
          current[len] = '\0';
          if (strcmp(current, smallest) < 0)
            strcpy(smallest, current);
        }
    }
  printf("%s\n", smallest);
}
