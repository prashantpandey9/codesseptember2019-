// exception handling
import java.util.Scanner;
class prg60
{
	public static void main(String[] args) {
		int a,b;
		int c=0;
		Scanner s=new Scanner(System.in);
		System.out.print("enter value for A : ");
		a=s.nextInt();
		System.out.print("enter value for B : ");
		b=s.nextInt();
		try
		{
			c=a/b;   //code that will raise exception
		}

		catch(ArithmeticException e)   //handling exception...
		{
			System.out.println("in arithmatic exception");
			System.out.println("technical message ::-"+  e.getMessage());
			System.out.println("\t Plzz enter any value for B except 0");
		}

		catch(Exception e)   //handling exception by parent
		{
			System.out.println("in parent Exception block");
			System.out.println("technical message ::-"+  e.getMessage());
			System.out.println("\t Plzz enter any value for B except 0");
		}
		
		 finally
		 {
			System.out.println("ans : "+c);
		}
	}
}