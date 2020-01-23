// calulate x^y before start the program
class prg51
{
	public static void main(String[] args) {
		int c=1;
		int a=Integer.parseInt(args[0]);
		int b=Integer.parseInt(args[1]);
		for(int i=1;i<=b;i++)
		{
			c=c*a;
		}

		System.out.println("ans : " + c);

	}
}
