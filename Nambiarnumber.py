Input Mismatch Error (Change to String)

import java.util.*;
import java.io.*;
public class Main
{
	public static void main(String[] args) 
	{
	    Scanner scn=new Scanner(System.in); 
	   int n=scn.nextInt();
	    int x=0;
	    int a[]=new int[n];
	    for(int i=0;i<n;i++)
	    {
	        if(a[i]%2==0 && a[i+1]%2==0)
	        {
	           a[i]+=a[i+1];
	        }
	        else
	        {
	            x=a[i+2]+a[i+3];
	        }
	        if(a[i]%2!=0 && a[i+1]%2!=0)
	        {
	           a[i]+=a[i+1];
	        }
	        else
	        {
	            x=a[i+2]+a[i+3];
	        }
	    }
	}
}
