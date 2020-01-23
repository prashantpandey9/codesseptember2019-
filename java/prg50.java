// add n number before start the program
class prg50
{
	public static void main(String[] args) {
		int c=0;
		for(int i=0;i<args.length;i++)
		{
			c=c+Integer.parseInt(args[i]);
		}

			System.out.println("result : " + c);

	}
}
