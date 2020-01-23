// game
import java.util.Scanner;
class Prg7
{
	public static void main(String... args)
	{
		int a;
		Scanner s=new Scanner(System.in);
		System.out.println("Enter your lucky number in between 1 to 3");
		a=s.nextInt();
		switch(a)
		{
			case 1:
			   System.out.println("you win laptop");
			   break;
			case 2:
			    System.out.println("you win bike");
			    break;
			case 3:
			   System.out.println("better luck next time");
			   break;
			default :
			   System.out.println("plese enter valid number ");
		}
	}
}