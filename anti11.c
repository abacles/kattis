#include <stdio.h>

#define BIG 1000000007

int main()
{
  int cases,len,good[10001] = {0,2,3},next = 3,i;
  scanf("%d",&cases);
  for(i=0;i<cases;i++)
  {
    scanf("%d",&len);
    for(;next<=len;next++)
      good[next] = (good[next-1] + good[next-2]) % BIG;
    printf("%d\n",good[len]);
  }
}
