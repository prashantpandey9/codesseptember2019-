// matrix multiplication
import java.util.Scanner;
class Prg24
{
	public static void main(String... args)
	{
		int[][] a=new int[3][3];
		int[][] b=new int[3][3];
		int[][] c=new int[3][3];
		Scanner s=new Scanner(System.in);
		int i,j,k,sum;
		System.out.println("Enter first array's element :");
		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				a[i][j]=s.nextInt();
		System.out.println("Enter second array's element :");
		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				a[i][j]=s.nextInt();
		
		System.out.println("After multiplication Array : ");
		for(i=0;i<3;i++)
		{
			for (j=0;j<3;j++)
			{
				sum=0;
				for(k=0;k<3;k++)
                    sum=sum+a[i][k]+b[k][j];
                c[i][j]=sum;

			}
			
		}
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
				System.out.print("\t"+c[i][j]);
			System.out.println("");
		}
	}
}