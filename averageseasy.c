#include <stdio.h>

int main()
{
  int ncases, ncs, neco, csiq[200000], i, j, k;
  double csavg, ecoavg;
  scanf("%d", &ncases);
  for(i=0;i<ncases;i++)
    {
      scanf("%d %d", &ncs, &neco);
      for(j=csavg=0;j<ncs;csavg=((csavg*j)+csiq[j])/(++j))
        scanf("%d", &csiq[j]);
      for(j=ecoavg=0;j<neco;ecoavg=((ecoavg*j)+k)/(++j))
        scanf("%d", &k);
      for(j=k=0;j<ncs;j++)
        {
          if(ecoavg < csiq[j] && csiq[j] < csavg)
            k++;
        }
      printf("%d\n", k);
    }
}
