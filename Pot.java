import java.util.Scanner;

public class Pot
{

    public static void main(String [] args)
    {
        Scanner scan=new Scanner(System.in);
        int potcount=scan.nextInt();
        int unproc []=new int [potcount];
        long proc []=new long [potcount];
        long sum=0;
        int i;
        for(i=0;i<potcount;i++)
	    {
		unproc [i]=scan.nextInt();
		proc [i]=(long)Math.pow(unproc [i]/10, unproc [i]%10);
		sum+=proc [i];
	    }
        System.out.println(sum);
        scan.close();
    }
    
}
