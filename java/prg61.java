// ArrayOutOfBoundIndex
import java.util.Scanner;
class prg61
{
	public static void main(String[] args) {
		try
		{
			int[] a={45,78,90,34};
			System.out.println(a[10]);  // throws the index which are be responsible for exception
		}
		catch(ArrayIndexOutOfBoundsException e)  // catch the index which are be responsible for exception
		{
			System.out.println(e.getMessage());
		}

		System.out.println("Happy Learning");
	}
}