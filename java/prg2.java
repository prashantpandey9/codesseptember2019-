//addition of two number
import java.util.Scanner;
class Prg2
{
	public static void main(String... argv)
	{
		Scanner obj=new Scanner(System.in);
		System.out.println("enter first number");
		int a=obj.nextInt();
		System.out.println("enter second number");
		int b=obj.nextInt();
		int c=a+b;
		System.out.println("sum of "+a+" and "+b+" is "+c);
	}
}