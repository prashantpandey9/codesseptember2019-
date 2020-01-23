// exception handling
import java.util.Scanner;
class prg58
{
	public static void main(String[] args) {
		float a,b;
		float c=0;
		Scanner s=new Scanner(System.in);
		System.out.print("enter value for A : ");
		a=s.nextFloat();
		System.out.print("enter value for B : ");
		b=s.nextFloat();
		try
		{
			c=a/b;   //code that will raise exception
			System.out.println("ans : "+c);
		}
		catch(ArithmeticException e)   //handling exception...
		{
			System.out.println("technical message ::-"+e);
			System.out.println("technical message ::-"+  e.getMessage());
			System.out.println("\t Plzz enter any value for B except 0");
		}
		 finally
		 {
			System.out.println("ans : "+c);
		}
	}
}