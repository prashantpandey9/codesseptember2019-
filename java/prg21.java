// jagged array
import java.util.Scanner;
class Prg21
{
	public static void main(String... args)
	{
		int[][] a=new int[3][];  //jageed array
	    a[0]=new int[5];
		a[1]=new int[9];
		a[2]=new int[3];

		for(int i=0;i<a.length;i++)
		{
			for(int j=0;j<a[i].length;j++)
                System.out.print(" "+a[i][j]);

            System.out.println("");
		}

	}
}