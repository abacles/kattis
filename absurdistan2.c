#include <stdio.h>

long int power(int base,int exp)
{
  if(exp==1)
    return base;
  else
    return base*power(base,exp-1);
}

long int select(int total,int choose)
{
  int poss=1;
  int i;
  for(i=0;i<choose;i++)
    poss*=total-i;
  for(;choose>1;choose--)
    poss/=choose;
  return poss;
}

int main()
{
  long long int cc_comb [140]={-1};
  int cities,i,j;
  long double prob;
  cc_comb [1]=1;
  cc_comb [2]=8;
  scanf("%d",&cities);
  for(i=3;i<cities;i++)
    {
      cc_comb [i]=power(i,i+1);
      for(j=1;j<i-1;j++)
	{
	  cc_comb [i]-=select(i,j)*(cc_comb [j]*power(i-j-1,i-j));
	}
    }
  printf("%lld\n",cc_comb [cities-1]);
  prob=(long double)cc_comb [cities-1]/power(cities-1,cities);
  printf("%.10Lf\n",prob);
  return 0;
}
