import java.util.Scanner;

class Cold
{
    public static void main(String args [])
    {
	Scanner scan=new Scanner(System.in);
	int temp_count=scan.nextInt();
	int cold=0;
	int i;
	for(i=0;i<temp_count;i++)
	    {
		if(scan.nextLong()<0)
		    cold++;
	    }
	System.out.println(cold);
    }
}
