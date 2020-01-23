// sum two integers and four integers
import java.util.Scanner;
class add
{
	int two(int x,int y)
	{
		return x+y;
	}
	int four(int a,int b,int c,int d)
	{
		return a+b+c+d;
	}

}

class Prg30
{
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		int a,b;
		int p,q,x,y;
		add sum =new add();
		System.out.println("Enter two number ");
		a=s.nextInt();
		b=s.nextInt();
		System.out.println("sum of "+a+" and "+b+" is "+sum.two(a,b));

        
		System.out.println("Enter four number ");
		p=s.nextInt();
		q=s.nextInt();
		x=s.nextInt();
		y=s.nextInt();
		System.out.println("sum is "+sum.four(p,q,x,y));
	}
}