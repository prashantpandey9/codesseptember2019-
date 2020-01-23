// exception throw
import java.util.Scanner;
class prg59
{
	public static void main(String[] args) {
		int a,b;
		int c=0;
		Scanner s=new Scanner(System.in);
		System.out.print("enter value for A : ");
		a=s.nextInt();
		System.out.print("enter value for B : ");
		b=s.nextInt();
		
			c=a/b;
		
			System.out.println("ans : "+c);
	}
}