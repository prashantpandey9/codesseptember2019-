// sum of diagonal element in 2-D array
import java.util.Scanner;
class Prg23
{
	public static void main(String... args)
	{
		int[][] a=new int[5][5];
		System.out.println("Enter array element for 5*5 :");
		Scanner s=new Scanner(System.in);
		int i,j,sum=0;
		for(i=0;i<5;i++)
			for(j=0;j<5;j++)
				a[i][j]=s.nextInt();
		System.out.println("Array : ");
		for(i=0;i<5;i++)
		{
			for (j=0;j<5;j++ )
			{
				if(i==j || j==4-i)
				sum+=a[i][j];
				System.out.print("\t"+a[i][j]+"\t");
			}
			System.out.println("");
		}
        System.out.println("\nsum of array's element is : "+sum);
	}
}