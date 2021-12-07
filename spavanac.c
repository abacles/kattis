#include <stdio.h>

int adjusted_hour(int curr,int add)
{
  return (curr+24+add)%24;
}

int main()
{
  int hour,minute;
  scanf("%d %d",&hour,&minute);
  hour=adjusted_hour(hour,-1);
  minute+=15;
  if(minute>=60)
    {
      minute%=60;
      hour=adjusted_hour(hour,1);
    }
  printf("%d %d\n",hour,minute);
  return 0;
}
