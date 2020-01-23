// dynamic polymorphism
class dpoly_a
{
	void fun()
	{
		System.out.println("in class a ");
	}

}

class dpoly_b extends dpoly_a
{
	void fun()
	{
		System.out.println("in class b");
	}
}
class dpoly_c extends dpoly_a
{
	void fun()
	{
		System.out.println("in class c");
	}
}


class prg47
{
	public static void main(String[] args) {
		dpoly_a obj=new dpoly_a();
		obj.fun();
		obj=new dpoly_b();
		obj.fun();
		obj=new dpoly_c();
		obj.fun();
	}
}