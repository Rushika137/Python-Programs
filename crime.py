n=99
digit_sum=0
product_sum=1
temp=n
while n>0:
            digit_sum=digit_sum+(n%10)
            product_sum=product_sum*(n%10)
            n=n//10
print(digit_sum)
print(product_sum)
sum_of_both=digit_sum+product_sum
if temp%sum_of_both==0:
           print("True")
else:
        print("False")
         
