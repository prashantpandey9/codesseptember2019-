// accessing private data indirectly
class access_a
{
	private void get1()
	{
		System.out.println("in get1 method");
	}

	void get3()
	{
		System.out.println("in get3 method");
		get1();
	}
}

class acess_b extends access_a
{
	void get2()
	{
	    System.out.println("in get2");	
	}
}
class Prg36
{
	public static void main(String[] args) {
		acess_b o=new acess_b();
		o.get2();
		o.get3();
		// o.get1();  private data can't be access directly  
	}
}