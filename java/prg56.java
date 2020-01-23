// define method in interface or method defination in interface
interface d_method
{
	void fun();
	default void myfun()
	{
		System.out.println("in interface myfun method");
	}
	default void fun1()
	{
		System.out.println("in unterface, fun1 method");
	}
}
class d_2 implements d_method
{
	public void fun()  // can't change the signature of the method in overriding so use public
	{
		System.out.println("in fun method");
	}

	public void fun1()    // we can override method defination which will defined in interface
	{
		System.out.println("in class, fun1");
	}
}
class prg56 extends d_2
{
	public static void main(String[] args) {
		d_method d=new d_2();  // reference variablo of d_method and creating object of class d_2
		d.fun();
		d.myfun();
		d.fun1();
	}
}