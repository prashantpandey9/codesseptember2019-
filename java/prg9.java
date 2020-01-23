// sum of digit of the given number
import java.util.Scanner;
class Prg9
{
	public static void main(String[] args) 
	{
		Scanner s=new Scanner(System.in);
		System.out.println("Enter four digit number");
		int a=s.nextInt();
		int sum=0,n;
		while(a!=0)
		{
			n=a%10;
			sum=sum+n;
			a=a/10;
		}
		System.out.println("sum of digit of the given number is "+sum);

	}
}