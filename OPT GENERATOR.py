import random
Alpha_list=['A-','B-','C-','D-','E-','F-','G-','H-','I-','J-','K-','L-','M-','N-','O-','P-','Q-','R-','S-','T-','U-','V-','W-','X-','Y-','Z-']
Digit_list=['0','1','2','3','4','5','6','7','8','9']
OTP=[]
Final_OTP=''
alpha_count=int(input("Enter how many alphabets count you want in OTP: "))
digit_count=int(input("Enter how many digit count you want in OTP: "))
for i in range(alpha_count):
    value=random.choice(Alpha_list)
    OTP.append(value)
for i in range(digit_count):
    value=random.choice(Digit_list)
    OTP.append(value)
for i in OTP:
    Final_OTP = Final_OTP+str(i)

print(f"Your OTP is: {Final_OTP}")
    
