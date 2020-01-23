// multiple exception
import java.util.Scanner;
class prg62
{
	public static void main(String[] args) {
		try
		{
			int[] a=new int[5];
			a[6]=45/0;
		}
		

		catch(ArrayIndexOutOfBoundsException e)  
		{
			System.out.println("ArrayIndexOutOfBoundsException occur");
		}

		catch(ArithmeticException e) 
		{
			System.out.println("ArithmeticException occur");
		}

		catch(Exception e) 
		{
			System.out.println("parent exception occur");
		}

		System.out.println("Happy Learning");
	}
}