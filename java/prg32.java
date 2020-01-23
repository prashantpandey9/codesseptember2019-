// 2d jagged aaray traverse by for-each loop
class Prg32
{
	public static void main(String[] args) {
		int[][] a=new int[3][5];
		System.out.println(a.length);
		System.out.println(a[0].length);


    //for zig- zag array
     int [][]b=new int [3][];
     b[0]=new int[5];
     b[1]=new int[2];
     b[2]=new int[3];


     System.out.println(b.length);
	 System.out.println(b[0].length);
     System.out.println(b[1].length);
     System.out.println(b[2].length);


     for(int[] i:b)
     {
     	for(int j:i)
     		System.out.print(" "+j);
     	System.out.println();
     }


	}


}