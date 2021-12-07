#include <stdio.h>

int main()
{
  char alpha[26],ch,pan;
  int cases,i,j;
  scanf("%d%c",&cases,&ch);
  for(i=0;i<cases;i++)
    {
      for(j=0;j<26;j++) alpha[j] = 0;
      for(j=0;(ch = getchar()) != '\n';)
	{
	  if('A' <= ch && ch <= 'Z') ch += 32;
	  if('a' <= ch && ch <= 'z') alpha[ch-'a'] = 1;
	}
      for(pan=1,j=0;j<26;j++)
	{
	  if(!alpha[j])
	    {
	      pan = 0;
	      break;
	    }
	}
      if(pan) printf("pangram\n");
      else
	{
	  printf("missing ");
	  for(j=0;j<26;j++)
	    if(!alpha[j]) putchar('a'+j);
	  putchar('\n');
	}
    }
}
