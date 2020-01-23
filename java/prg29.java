// area
import java.util.Scanner;
class myarea
{
	   double carea(int r)
	   {
	   	    return (3.14*r*r);
	   } 
	   double cyarea(int r, int h)
	   {
	   	   return (2*3.14*r*h);
	   }

}

class Prg29
{
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		System.out.println("For Circle : ");
		System.out.print("Enter radius : ");
		int r=s.nextInt();

		myarea ma=new myarea();
		
		System.out.println("Area of circle : "+ma.carea(r));

		System.out.println("For cylender : ");

		System.out.print("enter radius : ");
		int rs=s.nextInt();
		System.out.print("enter height : ");
		int h=s.nextInt();
        
		System.out.println("Area of cylender : "+ma.cyarea(rs,h));
	}
}