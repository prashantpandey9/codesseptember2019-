// abstract class
abstract class abs_c_a
{
	void fun()
	{
		System.out.println("in class a ");
	}
}

class abs_c_b extends abs_c_a
{
	void fun1()
	{
		System.out.println("in class b");
	}
}
class prg45
{
	public static void main(String[] args) {

        // we can't be create abstract class's object
		//abs_c_a o=new abs_c_a();
		//o.fun();
		abs_c_b obj=new abs_c_b();
		obj.fun();
		obj.fun1();
	}
}