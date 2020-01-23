// sum of 1-D array element
import java.util.Scanner;
class Prg20
{
	public static void main(String... args)
	{
		int a[]=new int[10];
		int i,s=0;
		Scanner sc=new Scanner(System.in);

        System.out.println("Enter ten values :");
		for(i=0;i<10;i++)
			a[i]=sc.nextInt();

		for(i=0;i<10;i++)
			s=s+a[i];

        System.out.println("sum is "+s);
	}
}