#include <stdio.h>
#include <math.h>

float posroot(float a, float b, float c)
{
  return (-b + sqrt(b*b - 4*a*c)) / (2*a);
}

int main()
{
  float leakloc, leaksp, raintime, waittime, finlvl, extra, hi;
  scanf("%f %f %f %f %f", &leakloc, &leaksp, &raintime, &waittime, &finlvl);
  if(finlvl < leakloc)
    printf("%f %f\n", finlvl, finlvl);
  else
    {
      extra = finlvl - leakloc + waittime * leaksp;
      hi = raintime * posroot(raintime, -(leakloc+leaksp*raintime+extra), leaksp*leakloc);
      if(finlvl > leakloc)
	printf("%f %f\n", hi, hi);
      else
	printf("%f %f\n", leakloc, hi);
    }
}
