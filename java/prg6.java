// calculate percentage
import java.util.Scanner;
class Prg6
{
	public static void main(String... argv)
	{
		Scanner obj=new Scanner(System.in);
		int s=0,k;
		System.out.println("enter name : ");
		String a=obj.nextLine();
		System.out.println("enter marks of 5 subject : ");
		for(int i=0;i<5;i++)
		{
			int b=obj.nextInt();
		     s=s+b;
		}
		k=s/5;
		System.out.println(a);
   		System.out.println("percentage "+k+"%");
        
		if(k<33)
		{
      		System.out.println("division : fail");
		}
		else if(k>=60)
			System.out.println("division : 1st");
		else if(k>45 && k<60)
        {
           System.out.println("division : 2nd");
        }
        else
        	System.out.println("division : 3rd");
	}
}