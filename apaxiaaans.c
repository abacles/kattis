#include <stdio.h>

int main()
{
  char name[251],new[251];
  int i,w=0;
  scanf("%s",name);
  new[w++] = name[0];
  for(i=1;name[i];i++)
    {
      if(name[i] != name[i-1])
	new[w++] = name[i];
    }
  new[w] = 0;
  printf("%s\n",new);
}
