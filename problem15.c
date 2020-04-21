#include <stdio.h>
#include <stdlib.h>
#include <math.h>
float f(float t ,float y);
float exact_solution(float t);

int main()
{
	float t, t1 = 0 ,t2 = 2 ,y1 = 0.5 , y ,h =0.2 ,error_bound , error;
    
    t = t1;
    y = y1;

    while (t <= t2 + h)
    {
       error = (exact_solution(t) - y);
       // formula of error bound calculated 
       error_bound = (exp(t) - 1) * 0.1 * (0.5 * exp(2) - 2);
       printf(" Error at the point t = %f is %f \n",t ,error );
       printf(" Error Bound at the mesh point t = %f is %f \n\n",t ,error_bound );
       y = y + h * f(t , y); t = t + h ;

    }
	return 0;
}

// definition of dy/dt(t,y)
float f(float t ,float y)
{
	return (y - t * t + 1);
}

float exact_solution(float t)
{
  return  ((t + 1) * (t + 1) - 0.5 * exp(t));
}
