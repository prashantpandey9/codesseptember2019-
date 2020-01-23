//swapping without using 3rd variable
import java.util.Scanner;
class Prg5
{
	public static void main(String... argv)
	{
		Scanner obj=new Scanner(System.in);
		System.out.println("enter first number");
		int a=obj.nextInt();
		System.out.println("enter second number");
		int b=obj.nextInt();
		a=a+b;
		b=a-b;
		a=a-b;
		System.out.println("a : "+a+" b : "+b);
	}
}