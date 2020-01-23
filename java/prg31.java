// static test
class static_test
{
	int s=10;
	static int p=20;

}

class Prg31
{
	public static void main(String[] args) {

	   System.out.println("p is static instance "+static_test.p);	

	   static_test st=new static_test();

	   System.out.println("s is non-static instance "+st.s);	

	}
}