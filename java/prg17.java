// constructor overloading
class cons
{
    cons()
    {
        System.out.println("hey! you inside constructor");
    }
    cons(int n)
   {
      System.out.println("n : "+n);
   }
}
class Prg17
{
	public static void main(String... args)
	{
                       cons c=new cons(23);
                       System.out.println("inside main method");
                  }
}