// sum of two 2-D array's elements
import java.util.Scanner;
class Prg22
{
	public static void main(String... args)
	{
		int[][] a=new int[3][3];
		int[][] b=new int[3][3];
		int[][] c=new int[3][3];
		Scanner s=new Scanner(System.in);
		int i,j;
		System.out.println("Enter first array's element :");
		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				a[i][j]=s.nextInt();
		System.out.println("Enter second array's element :");
		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				b[i][j]=s.nextInt();
		
		System.out.println("After addition Array : ");
		for(i=0;i<3;i++)
			for (j=0;j<3;j++)
		        c[i][j]=a[i][j]+b[i][j];
		
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
				System.out.print("\t"+c[i][j]);
			System.out.println("");
		}
	}
}