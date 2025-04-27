import re
import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(8))

def process_text(text):
    email_pattern = r'\b([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b'
    
    email_matches = re.finditer(email_pattern, text)
    
    results = []
    for match in email_matches:
        username = match.group(1)  
        full_email = match.group(0) 
        password = generate_password()
        
        results.append(f"{full_email} username: {username}, password: {password}")
    
    return results

sample_text = """Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari"""

for result in process_text(sample_text):
    print(result)