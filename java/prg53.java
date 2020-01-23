// multiple interface
interface i1
{
	void fun1();
}

interface i2
{
	void fun2();
}
class inter_a implements i1,i2
{
	public void fun1()
	{
		System.out.println("hii");
	}
	public void fun2()
	{
		System.out.println("hello");
	}
}

class prg53
{
	public static void main(String[] args) {
		inter_a o1=new inter_a();
		o1.fun1();
		o1.fun2();
	}
}