// calulate sum at start the program or at run time
import java.util.Scanner;
class prg52
{
	public static void main(String[] args) {
		int c=0;
		if(args.length!=0)
		{
			for(int i=0;i<args.length;i++)
				c=c+Integer.parseInt(args[i]);
		}
		else
		{
			System.out.println("Enter two number : ");
			Scanner s=new Scanner(System.in);
			int a=s.nextInt();
			int b=s.nextInt();
			c=a+b;
		}

		System.out.println("sum : " + c);

	}
}
