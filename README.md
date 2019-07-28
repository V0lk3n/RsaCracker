# RsaCracker
Two script who allow you to crack RSA. Used for the peaCTF2019 RSA challenge.

# Writeup of the challenge where the tools are used
PDF : https://github.com/SinHackTeam/writeup/blob/master/peaCTF2019/Round%201/Cryptography/rsa-volken-writeup.pdf <br>
Video : https://www.youtube.com/watch?v=iNTgZPX9EFw&list=PLh8tcFejqvOzWxLj5M_IdSltiukRQZZo1&index=4 <br>

# How to (rsa_part1.py)

# Install libctf
git clone https://github.com/arisada/libctf.git<br>
export PYTHONPATH=/full/path/of/libctf<br>

# Factoring n for have p and q value.
Go to this website : https://www.alpertron.com.ar/ECM.HTM<br>
Copy paste you'r n value, then click on "Factor" button, wait a moment and you will have p and q value separate by an "x"<br>
Example : 404796 306518 120759 733507 156677 × 408801 179738 927870 766525 808109<br>
Remove the space!<br>

# Run the script
python rsa_part1.py<br>
copy paste the value when asked<br>



# How to (rsa_part2.py)

# Install libctf
git clone https://github.com/arisada/libctf.git<br>
export PYTHONPATH=/full/path/of/libctf<br>

# Run the script
python rsa_part2.py<br>
copy paste the value when asked<br>
