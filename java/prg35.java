// method oveloading in inheritance
import java.util.Scanner;
class c_area
{
	double area(int r)
	{
		return 3.14*r*r;
	}
}
class r_area extends c_area
{
	int area(int l,int b)
	{
		return l*b;
	}
	double area(double a,double b,double c)
	{
		double s=(a+b+c)/2;
		double p=s*(s-a)*(s-b)*(s-c);
		double k=java.lang.Math.sqrt(p);
		return k;
	}
}

class Prg35
{
	public static void main(String[] args) {
		r_area obj=new r_area();
		Scanner sc=new Scanner(System.in);
		System.out.println("For Circle");
		System.out.print("Enter radius : ");
		int rc=sc.nextInt();
		System.out.println("Area of circle : "+obj.area(rc));

		System.out.println("For Rectangle");
		System.out.print("Enter length : ");
		int l=sc.nextInt();
		System.out.print("Enter breadth : ");
		int b=sc.nextInt();
		System.out.println("Area of Rectangle : "+obj.area(l,b));

		System.out.println("For Triangle");
		System.out.print("Enter three sides  : ");
		double a=sc.nextDouble();
		double ab=sc.nextDouble();
		double c=sc.nextDouble();
		if(obj.area(a,ab,c)>0)
		    System.out.println("Area of Triangle : "+obj.area(a,ab,c));
	    else
	    	System.out.println("Triangle not be formed");
	}
}