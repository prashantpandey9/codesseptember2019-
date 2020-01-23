// explicitly constructor changing by super
class construc1
{
	construc1(int a,int b)
	{
		System.out.println(a+b);
	}
}
class construc2 extends constr1
{
	construc2(int x,int y,int z)
	{
		super(x,y);
		System.out.println(x+y+z);
	}
}

class Prg39
{
	public static void main(String[] args) {
		construc2 obj =new construc2(10,20,30);
	}
}