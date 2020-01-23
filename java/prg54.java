// if method name is same, both in interface
interface i1
{
	void fun();
}

interface i2
{
	void fun();
}
class inter_a implements i1,i2
{
	public void fun()
	{
		System.out.println("hii");
	}
}

class prg54
{
	public static void main(String[] args) {
		inter_a o1=new inter_a();
		o1.fun();
	}
}