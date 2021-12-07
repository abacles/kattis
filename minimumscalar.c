#include <stdio.h>
#include <stdlib.h>

int compar(const void *a,const void *b)
{
  return *(int*)a - *(int*)b;
}

int main()
{
  int cases,c,size,a[800],b[800],i;
  long long int prod;
  scanf("%d",&cases);
  for(c=0;c<cases;c++)
    {
      scanf("%d",&size);
      for(i=0;i<size;i++) scanf("%d",&a[i]);
      for(i=0;i<size;i++) scanf("%d",&b[i]);
      qsort(a,size,sizeof(int),compar);
      qsort(b,size,sizeof(int),compar);
      for(prod=0,i=0;i<size;i++)
	prod += (long long int)(a[i]) * (b[size-i-1]);
      printf("Case #%d: %lld\n",c+1,prod);
    }
}
