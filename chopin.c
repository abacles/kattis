#include <stdio.h>
#include <string.h>

int main()
{
  int c;
  char note[3],tonality[6];
  for(c=1;scanf("%s %s",note,tonality) != EOF;c++)
    {
      if(!strcmp(note,"A#"))
	printf("Case %d: Bb %s\n",c,tonality);
      else if(!strcmp(note,"Bb"))
	printf("Case %d: A# %s\n",c,tonality);
      else if(!strcmp(note,"C#"))
	printf("Case %d: Db %s\n",c,tonality);
      else if(!strcmp(note,"Db"))
	printf("Case %d: C# %s\n",c,tonality);
      else if(!strcmp(note,"D#"))
	printf("Case %d: Eb %s\n",c,tonality);
      else if(!strcmp(note,"Eb"))
	printf("Case %d: D# %s\n",c,tonality);
      else if(!strcmp(note,"F#"))
	printf("Case %d: Gb %s\n",c,tonality);
      else if(!strcmp(note,"Gb"))
	printf("Case %d: F# %s\n",c,tonality);
      else if(!strcmp(note,"G#"))
	printf("Case %d: Ab %s\n",c,tonality);
      else if(!strcmp(note,"Ab"))
	printf("Case %d: G# %s\n",c,tonality);
      else
	printf("Case %d: UNIQUE\n",c);
    }
}
