// accessing protected default public member in same package and same program
class hii
{
	private int a;
	protected int pixie=20;
	int myp=30;
	public int yourp=50;
}
class hello
{
	hii obj =new hii();
	hello()
	{
	//System.out.println("a : "+obj.a);
	System.out.println("b : "+obj.pixie);
	System.out.println("c : "+obj.myp);
	System.out.println("d : "+obj.yourp);
    }
}
class Prg33
{
	public static void main(String[] args) {
		hello ob=new hello();
	}
}