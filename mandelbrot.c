#include <stdio.h>
#include <math.h>

int main()
{
	double x, y, ox, oy, tmp;
	int r, c = 0;
	while(scanf("%lf %lf %d", &ox, &oy, &r) != EOF)
	{
		x = y = 0;
		while(r--)
		{
			tmp = x;
			x = x*x - y*y + ox;
			y = 2*tmp*y + oy;
			if(hypot(x, y) > 2)
				break;
		}
		printf("Case %d: %s\n", ++c, hypot(x, y) > 2 ? "OUT":"IN");
	}
}
