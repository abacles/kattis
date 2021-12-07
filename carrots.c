#include <stdio.h>

int main()
{
  long long int n,i;
  int solved;
  char foo;
  scanf("%lld %d",&n,&solved);
  getchar();
  for(i=0;i<n;i++)
    {
      while((foo=getchar())!='\n') {}
    }
  printf("%d\n",solved);
  return 0;
}
