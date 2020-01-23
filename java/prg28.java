//reverese number
import java.util.Scanner;
class test
{
	int num;
	test(int n)
	{
		num=n;
	}
	public int getReverse()
	{
		int s=0,p;
		while(num!=0)
		{
			p=num%10;
			s=(s*10)+p;
			num=num/10;
		}
		return s;
	}

}

class Prg28
{
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		System.out.print("Enter a number : ");
		int k=s.nextInt();
		test t=new test(k);
		System.out.println("given number : "+k);
		System.out.println("reverse number : "+t.getReverse());
	}
}