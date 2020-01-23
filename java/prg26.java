// searching
import java.util.Scanner;
class Prg26
{
	public static void main(String... args)
	{
		Scanner s=new Scanner(System.in);
		int[] a=new int[10];
		int i;
		System.out.println("Enter array element");
		for(i=0;i<10;i++)
			a[i]=s.nextInt();

		System.out.println("Enter searching element");
		int k;
		k=s.nextInt();
		
		for(i=0;i<10;i++)
		{
			if(a[i]==k)
			{
				System.out.println("element found at "+i+" index");
				break;
			}
		}
		if(i==10)
			System.out.println("element not found");
	}
}