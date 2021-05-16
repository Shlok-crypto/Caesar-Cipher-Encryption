# Caesar-Cipher-Encryption

The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of **substitution cipher**, i.e., each letter of a given text is replaced by a letter some _fixed number of positions_ down the alphabet.

# Input: 
* A String of Lower and or Upper case letters, called Text.
* An Integer between 0-25 denoting the required shift.

# Output 
* A Completely New String predefined with Interger Shift 

# Example 
![image](https://user-images.githubusercontent.com/83566027/118398599-f9e71800-b676-11eb-8561-d41909a5347e.png)


# Encryption
Encryption of a letter by a shift n can be described mathematically as. 
 
**E_n(x)=(x+n)mod\ 26**
(Encryption Phase with shift n)

![image](https://user-images.githubusercontent.com/83566027/118398585-e63bb180-b676-11eb-96fa-305140d127e6.png)

# Decryption 
Dcryption of a letter by a shift n can be described mathematically as.


**D_n(x)=(x-n)mod\ 26**
(Decryption Phase with shift n)

This is the Reverse Mathemetical representation of the Encryption 
The correct Shift integer value and utlizing the equation, you can decode the Encrypted Text 
