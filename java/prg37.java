// method chaining
class chain_a
{
	void get()
	{
		System.out.println("in base class");
	}
}

class chain_b extends chain_a
{
	void get()
	{
		super.get();  // call parent's function
		System.out.println("in derived class");
	}
}
class Prg37
{
	public static void main(String[] args) {
		chain_b o=new chain_b();
		o.get();
	}
}