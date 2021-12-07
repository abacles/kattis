#include <stdio.h>
#include <math.h>

#define INF 100000000
#define UNZIP(T, C) T[C[0]-'A'][C[1]-'A'][C[2]-'A']

int negcyc(double g[200][200], int n)
{
	int i, j, k;
	for(k=0;k<n;k++)
	{
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(g[i][k] != INF && g[k][j] != INF && g[i][k]+g[k][j] < g[i][j])
					g[i][j] = g[i][k] + g[k][j];
			}
		}
	}
	for(i=0;i<n;i++)
	{
		if(g[i][i] < 0)
			return 1;
	}
	return 0;
}

int main()
{
	int ncurrencies, nx, rfrom, rto, ctoi[26][26][26], i, j;
	char ccode[4], cfrom[4], cto[4];
	double xrates[200][200]; 
	while(scanf("%d", &ncurrencies), ncurrencies != 0)
	{
		for(i=0;i<ncurrencies;i++)
		{
			scanf("%s", ccode);
			UNZIP(ctoi, ccode) = i;
			for(j=0;j<ncurrencies;j++)
				xrates[i][j] = i == j ? 1 : INF;
		}
		scanf("%d", &nx);
		for(i=0;i<nx;i++)
		{
			scanf("%s %s %d:%d", cfrom, cto, &rfrom, &rto);
			xrates[UNZIP(ctoi, cfrom)][UNZIP(ctoi, cto)] = -log(1.0*rto/rfrom);
		}
		printf("%s\n", negcyc(xrates, ncurrencies) ? "Arbitrage" : "Ok");
	}
}
