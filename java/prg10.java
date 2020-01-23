// calculate factorial
import java.util.Scanner;
class Prg10
{
	public static void main(String[] args) 
	{
	      Scanner s=new Scanner(System.in);
	      System.out.println("enter a number");
	      int a=s.nextInt();
          int k=1;
	      for(int i=a;i>=1;i--)
	      {
	      	k=k*i;
	      }
	      System.out.println("factorial is "+k);

	}
}