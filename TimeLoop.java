import java.util.Scanner;

public class TimeLoop
{

    public static void main(String [] args)
    {
        Scanner scan=new Scanner(System.in);
        int iter=scan.nextInt();
        int i;
        for(i=0;i<iter;i++)
            System.out.println(i+1+" Abracadabra");
        scan.close();
    }
    
}
