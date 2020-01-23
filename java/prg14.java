// count vowels and consonant
import java.util.Scanner;
class Prg14
{
	public static void main(String[] args)
    {
    	Scanner s=new Scanner(System.in);
    	System.out.println("Enter your name");
    	String str=s.nextLine();
    	int v=0,c=0,p=0;
    	int l=str.length();
    	char[] ch=str.toCharArray();
    	for(int i=0;i<l;i++)
    	{
    		if(ch[i]=='a' || ch[i]=='e' || ch[i]=='i' || ch[i]=='o' || ch[i]=='u' || ch[i]=='A' || ch[i]=='E' || ch[i]=='I' || ch[i]=='O' || ch[i]=='U')
    	        v++;
    	    else if(ch[i]==' ')
    	    	p++;
    	    else 
    	    	c++;
    	}
    	System.out.println("no. of vowels "+v+" no. of consonant "+c);
	}
}

// boxing & unboxing		