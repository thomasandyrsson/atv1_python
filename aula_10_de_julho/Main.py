from Conta import Conta

#Instanciar novos objetos
c1 = Conta("Thomas Andersson", 2842.99)
c2 = Conta("Andersson Araujo", 1597.25)
c3 = Conta("João Alfredo", 0)

#novos depositos
c1.depositar(500)
c2.depositar(600)
c3.depositar(3500)

#novo saques
c1.sacar()
c2.sacar()
c3.sacar()

#informações
c1.imprimeDados()
c2.imprimeDados()
c3.imprimeDados()

#novos titulares
c1.setTitular("Robert De Niro")
c2.setTitular("Jennifer Anniston")
c3.setTitular("Adriane Matias")

#informações
c1.imprimeDados()
c2.imprimeDados()
c3.imprimeDados()