// check two array's elements are equal or not
import java.util.Scanner;
class Prg25
{
	public static void main(String... args)
	{
		Scanner s=new Scanner(System.in);
		int[] a=new int[5];
		int[] b=new int[5];
		int i;
		System.out.println("Enter 1st array element");
		for(i=0;i<5;i++)
			a[i]=s.nextInt();

		System.out.println("Enter 2nd array element");
		
		for(i=0;i<5;i++)
			b[i]=s.nextInt();
		for(i=0;i<5;i++)
		{
			if(a[i]!=b[i])
			{
				System.out.println("both array are different");
				break;
			}
		}
		if(i==5)
			System.out.println("both array same");
	}
}