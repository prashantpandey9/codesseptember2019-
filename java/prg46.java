// abstract method
abstract class absa
{
	void fun()
	{
		System.out.println("in class absa ");
	}

	abstract void fun1();
	abstract void fun2();
}

abstract class absb extends absa
{
	void fun1()
	{
		System.out.println("in fun1");
	}
}
class absc extends absb
{
	void fun2()
	{
		System.out.println("in fun2");
	}
}


class prg46
{
	public static void main(String[] args) {
		absc obj=new absc();
		obj.fun();
		obj.fun1();
		obj.fun2();
	}
}