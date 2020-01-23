// elligible for marraige
import java.util.Scanner;
class Prg8
{
	public static void main(String... args)
	{
		String name;
		char g;
		int age;
		Scanner s= new Scanner(System.in);
		System.out.println("enter your name");
		name=s.nextLine();
		System.out.println("enter your age");
		age=s.nextInt();
		System.out.println("enter your gender\nfor male press m \nfor female press f");
		g=s.next().charAt(0);
		if(g=='m' || g=='M')
		{
			if(age>=21)
				System.out.println("elligible for marriage");
			else
				System.out.println("not elligible for marriage so wait...");
		}
		else
		{
			if(age>=18)
				System.out.println("elligible for marriage");
			else
				System.out.println("not elligible for marriage so wait...");

		}
	}
}