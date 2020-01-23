// explicitly constructor changing
class constr1
{
	constr1()
	{
		System.out.println("call constr1");
	}
}
class constr2 extends constr1
{
	constr2()
	{
		System.out.println("call constr2");
	}
}
class constr3 extends constr2
{
	constr3()
	{
		System.out.println("call constr3");
	}
}

class Prg38
{
	public static void main(String[] args) {
		constr3 obj =new constr3();
	}
}