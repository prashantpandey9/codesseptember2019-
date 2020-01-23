// method overriding
class overrid_a
{
	void fun()
	{
		System.out.println("in class a");
	}
}
class overrid_b extends overrid_a
{
	void fun()
	{
		System.out.println("in class b");


		// for calling parent method then use super keyword

		super.fun();
	}
}

class prg44
{
	public static void main(String[] args) {
		overrid_b obj=new overrid_b();
		obj.fun();

	}
}