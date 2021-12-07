#include <stdio.h>

int main()
{
  int npoints, points[1000][2], area, i;
  while(scanf("%d",&npoints), npoints)
  {
    for(i=0;i<npoints;i++)
      scanf("%d %d", &points[i][0], &points[i][1]);
    for(area=0,i=0;i<npoints;i++)
      area += (points[i][0] * points[(i+1)%npoints][1] -
               points[i][1] * points[(i+1)%npoints][0]);
    if(area > 0)
      printf("CCW %.1f\n", area / 2.0);
    else
      printf("CW %.1f\n", area / -2.0);
  }
}
