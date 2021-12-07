#include <stdio.h>
#include <stdlib.h>

int abs(int n)
{
  if(n < 0)
    return -n;
  return n;
}

int comp(const void *a,const void *b)
{
  return abs(*(int*)a) - abs(*(int*)b);
}

int main()
{
  int dropcount,amount;
  int *pos,drink = 0,prev = 0;
  int i,t;
  scanf("%d %d",&dropcount,&amount);
  pos = malloc(sizeof(int)*dropcount);
  pos[0] = 0;
  for(i=0;i<dropcount;i++)
    scanf("%d",pos+i);
  for(i=0,t=0;i<dropcount;i++)
    {
      qsort(pos+i,dropcount-i,sizeof(int),comp);
      t += abs(pos[i]-prev);
      prev = pos[i];
      if(amount-t <= 0)
	break;
      drink += amount-t;
    }
  printf("%d\n",drink);
  free(pos);
  return 0;
}
