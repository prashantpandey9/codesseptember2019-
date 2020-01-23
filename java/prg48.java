// use final keyword
class final_a  // can't be inherited if class is final
{
	void fun()    // if it is final can't be override in class b and also in class c
	{
		System.out.println("in class a ");
	}

}

class final_b extends final_a
{
	void fun()    // if it is final can't be override in class c
	{
		System.out.println("in class b");
	}
}
class final_c extends final_b
{
	void fun()
	{
		System.out.println("in class c");
	}
}


class prg48
{
	public static void main(String[] args)
	 {
	 	int a=10;   // if it is final we can't be changed the value of a
	 	System.out.println("a : "+a);
	 	/* a=7;
	 	System.out.println("a : "+a);  */
		final_a obj=new final_a();
		obj.fun();
		obj=new final_b();
		obj.fun();
		obj=new final_c();
		obj.fun();
	}
}