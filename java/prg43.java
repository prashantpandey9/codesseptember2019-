// heirerchical inheritance

class inheri_a
{
	void fun()
	{
		System.out.println("in class inheri_a and method fun");
	}
}
class inheri_b extends inheri_a
{
	void fun1()
	{
		System.out.println("in class inheri_b and method fun1");
	}
}
class inheri_c extends inheri_a
{
	void fun2()
	{
		System.out.println("in class inheri_c and method fun2");
	}
}
class prg43
{
	public static void main(String[] args) {
		inheri_b o1=new inheri_b();
		o1.fun();
		o1.fun1();
		inheri_c o2=new inheri_c();
		o2.fun();
		o2.fun2();
	}
}