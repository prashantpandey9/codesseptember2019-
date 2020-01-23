// inheritance in interface
interface i1
{
	void fun1();
	void fun2();
}

interface i2 extends i1
{
	void fun3();
	void fun4();
}
class inheri_face implements i2
{
	public void fun1()
	{
		System.out.println("in fun1");
	}
	public void fun2()
	{
		System.out.println("in fun2");
	}
	public void fun3()
	{
		System.out.println("in fun3");
	}
	public void fun4()
	{
		System.out.println("in fun4");
	}
}

class prg55
{
	public static void main(String[] args) {
		inheri_face o1=new inheri_face();
		o1.fun1();
		o1.fun2();
		o1.fun3();
		o1.fun4();
	}
}