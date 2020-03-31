def check_fermat(a,b,c,n):
	if(n>2 and a**n+b**n==c**n):
			print('Holy smokes, Fermat was wrong!')
	else:
		print('No, that doesn’t work.')
a=input('input a')
b=input('input b')
c =input('input c')	
n= input('input n')
check_fermat(int(a),int(b),int(c),int(n))
#check_fermat(3,4,5,2)