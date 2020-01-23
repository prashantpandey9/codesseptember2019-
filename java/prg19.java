// 1D array
class Prg19
{
	public static void main(String... args)
	{
		int a[]=new int[5];
		int i;
		for(i=0;i<5;i++)
			System.out.println("a "+a[i]);

		int[] b=new int[5];
		for(i=0;i<5;i++)
			System.out.println("b "+b[i]);

		int[] c;
		c=new int[5];
		for(i=0;i<5;i++)
			System.out.println("c "+c[i]);
	}
}