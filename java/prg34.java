// is a relation
class mya
{
	void fun1()
	{
		System.out.println("in fun 1 and class mya");
	}
}
class myb extends mya
{
	void fun2()
	{
		System.out.println("in fun 2 and class myb");
	}
}

class Prg34
{
	public static void main(String[] args) {
		mya o1=new mya();
		myb o2=new myb();
		o1.fun1();
		o2.fun1();
		o2.fun2();
	}
}