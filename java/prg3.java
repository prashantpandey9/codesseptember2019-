//check even odd
import java.util.Scanner;
class Prg3
{
	public static void main(String... argv)
	{
		Scanner obj = new Scanner(System.in);
		System.out.println("Enter a number");
		int a=obj.nextInt();
		if(a%2==0)
			System.out.println("Even Number");
		else
			System.out.println("Odd Number");
	}
}