// armstrong number
import java.util.*;
class Prg16
{
	public static void main(String... args)
	{
		Scanner s=new Scanner(System.in);
		System.out.println("Enter range : ");
		int a=s.nextInt();
		int b=s.nextInt();
		int p,k,j;
		System.out.println("Armstong no. in between "+a+" and "+b+" is : ");
		for(int i=a;i<=b;i++)
		{
			k=i;
			j=0;
			while(k!=0)
			{
				p=k%10;
                j=j+(p*p*p);
                k=k/10;
			}

               // System.out.println(i+"\t"+j);
			if(j==i)
				System.out.println(i);
		}
	}
}