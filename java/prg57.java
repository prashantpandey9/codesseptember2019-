// create an static method in interface
interface i1
{
	void fun();
	static void fun1()
	{
		System.out.println("hello it is static method");
	}
    
}
class s_method implements i1
{
	public void fun()  
	{
		System.out.println("in fun method");
	}

}
class prg57 extends d_2
{
	public static void main(String[] args) {
	   s_method o=new s_method();
	   o.fun();
	   i1.fun1();
	}
}