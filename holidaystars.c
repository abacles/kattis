#include <stdio.h>
#include <math.h>

#define DELTA 0.001

double rad(int deg)
{
  return M_PI * deg / 180;
}

double angle(double x, double y, double cx, double cy)
{
  if(x == cx)
    return y > cy ? M_PI/2 : -M_PI/2;
  else if(x > cx)
    return atan((y - cy) / (x - cx));
  else
    return M_PI + atan((y - cy) / (x - cx));
}

int main()
{
  int n, theta, i, hit = 0;
  double w, v, vx, wall, poly[20][2], area = 0, cx = 0, cy = 0, r[20], prev[20], tmp, t;
  scanf("%d %lf %lf %d %lf", &n, &w, &v, &theta, &wall);
  for(i = 0; i < n; i++)
    scanf("%lf %lf", &poly[i][0], &poly[i][1]);
  for(i = 0; i < n; i++)
    {
      tmp = poly[i][0]*poly[(i+1)%n][1] - poly[(i+1)%n][0]*poly[i][1];
      area += 0.5 * tmp;
      cx += (poly[i][0]+poly[(i+1)%n][0]) * tmp;
      cy += (poly[i][1]+poly[(i+1)%n][1]) * tmp;
    }
  cx /= 6 * area;
  cy /= 6 * area;
  vx = v * cos(rad(theta));
  for(i = 0; i < n; i++)
    {
      r[i] = hypot(cx - poly[i][0], cy - poly[i][1]);
      prev[i] = angle(poly[i][0], poly[i][1], cx, cy);
    }
  for(t = 0; !hit; t += DELTA)
    {
      for(i = 0; i < n; i++)
	{
	  poly[i][0] += vx * DELTA;
	  poly[i][0] += (cos(prev[i] - w * DELTA) - cos(prev[i])) * r[i];
	  prev[i] -= w * DELTA;
	  if(poly[i][0] >= wall)
	    {
	      hit = 1;
	      break;
	    }
	}
    }
  printf("%d %f\n", i+1, t);
}
