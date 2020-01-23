// print employee data, taken by user
import java.util.Scanner;
class employee
{
	int eid;
	String name;
	String c_name;
	String founder;
	public void getData()
	{
		Scanner s=new Scanner(System.in);

		System.out.println("Enter your name");
		name=s.nextLine();
		System.out.println("Enter your company name");
		c_name=s.nextLine();
		System.out.println("Enter founder name");
		founder=s.nextLine();
		System.out.println("Enter your id");
        eid=s.nextInt();

	}
	public void disData()
	{

		System.out.println("id : "+eid);
		System.out.println("Name : "+name);
		System.out.println("company name : "+c_name);
		System.out.println("founder name : "+founder);
	}
}
class Prg15
{
	public static void main(String...args)
	{
		employee e=new employee();
		e.getData();
		e.disData();
	}
}