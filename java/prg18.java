// take 5 students data and print
import java.util.Scanner;
class student
{
	int roll;
	String name;
	static String course="core java";
	void setData()
	{
		Scanner s=new Scanner(System.in);
		System.out.println("Enter Rollno. : ");
		roll=s.nextInt();
		s.nextLine();          //for drop one input
		System.out.println("Enter Student name : ");
		name=s.nextLine();
	}
	void getData()
	{
		System.out.println("Rollno. : "+roll);
		System.out.println("Name : "+name);
		System.out.println("Course : "+student.course);
	}
}

class Prg18
{
	public static void main(String... args)
	{
		int i;
		student[] stu=new student[5];
		for(i=0;i<5;i++)
		{
			stu[i]=new student();
			stu[i].setData();
		}
		for(i=0;i<5;i++)
			stu[i].getData();
	}
}