import java.util.*;

public class YinYang
{
   public static void main(String[] args)
   {
      Scanner s = new Scanner(System.in);
      String stones = s.next();
      int b = 0, w = 0, i;
      for(i=0;i<stones.length();i++)
      {
         if(stones.charAt(i) == 'B')
            b++;
         else
            w++;
      }
      if(b == w)
         System.out.println("1");
      else
         System.out.println("0");
      s.close();
   }
}
