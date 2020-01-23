// for each loop
class Prg11
{
	public static void main(String[] args)
    {
		int []a={34,67,56,78};
		for(int i=0;i<a.length;i++)
			System.out.println(a[i]);
        System.out.println("");
// for each loop

    System.out.println("used by for each loop\n");
		for(int i:a)
			System.out.println(i);
	}
}

