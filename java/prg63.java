// implemnt runnable interface
class thread_1 implements Runnable
{
	public void run()
	{
		for(int i=0;i<10;i++)
			System.out.println("i "+i);
	}
}
class prg63
{
	public static void main(String[] args) {
		thread_1 t =new thread_1();
		Thread th=new Thread(t);
		th.start();
		for(int j=0;j<10;j++)
			System.out.println("j "+j);
	
	}
}