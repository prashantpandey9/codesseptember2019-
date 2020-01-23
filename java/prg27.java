// sorting
import java.util.Scanner;
class Prg27
{
	public static void main(String... args)
	{
		Scanner s=new Scanner(System.in);
		int n=5;
		int[] a=new int[n];
		int i,j;
		System.out.println("Enter 10 value for array element");
		for(i=0;i<n;i++)
			a[i]=s.nextInt();

		int temp;
		
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(a[i]>a[j])
				{
				   temp=a[i];
				   a[i]=a[j];
			       a[j]=temp;

				}
			}
			
		}
		for(i=0;i<n;i++)
			System.out.println(a[i]+" ");
	}
}