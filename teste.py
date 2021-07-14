import bcrypt

senha = "123456"

hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

print("\n\n senha: "+ senha + "   hash: "+ str(hash) + "\n\n")

x = "1234567"

if bcrypt.checkpw(x.encode(), hash):
    print("Senha certa")
else:
    print("Senha Invalida")
