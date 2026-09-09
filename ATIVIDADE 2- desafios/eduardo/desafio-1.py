#Lista dos alunos:

nomes = ["marcos", "eduardo", "pedro", "jhonatan", "menezes"]

print (nomes)

nomes.append("paula")
print (nomes)

nomes.remove("eduardo")
print (nomes)

nomes[2] = "lucas"  

print("3 primeiros:", nomes[:3])  
print("2 últimos:", nomes[-2:]) 

nomes.sort() 
print(nomes)

nomes.reverse()  
print(nomes)
