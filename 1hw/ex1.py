import numpy as np
Value=[0,1,2]
Cost=[0.25, 0.50,0]


n=Value[-1]
k=len(Cost)
Matrix=np.array(np.array([[0.00 for x in range(k)] for y in range(n+1)]))

for q in range(k,0,-1):
    for i in range(0,n+1):
        expected_value=0;
        for s in range(i+1,n+1):
            if q==k:
                expected_value+=Value[s]
            else:
                expected_value+=Matrix[s][q]
        if q==k:
            entry=max(i,((1/(n+1))*(expected_value+(i*(i+1)))-Cost[q-1]))
            Matrix[i][q-1]=entry
        else:
            entry=max(i,((1/(n + 1))*(expected_value+(Matrix[i][q]*(i+1)))-Cost[q-1]))
            Matrix[i][q-1]=entry


print(Matrix)
print("The expected revenue value is ", Matrix[0][0])

