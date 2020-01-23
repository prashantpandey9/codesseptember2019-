// implemnt multithreading
class thr_1 extends Thread
{
	public void run()
	{
		for(int i=0;i<5;i++)
			System.out.println("i "+i);
	}
}
class thr_2 extends Thread
{
	public void run()
	{
		for(int j=0;j<5;j++)
			System.out.println("j "+j);
	}
}
class prg64
{
	public static void main(String[] args) {

		thr_1 t1 =new thr_1();
		thr_2 t2 =new thr_2();
		Thread myt1=new Thread(t1);
		Thread myt2=new Thread(t2);
		myt1.start();
		myt2.start();
		for(int k=0;k<5;k++)
			System.out.println("k "+k);
	
	}
}