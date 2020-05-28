import turtle
import my_first_agent


def passo(agente):
    agente.fd(1)


def desenho(a1, a2, cor1, cor2):
    a1.fd(50)
    a1.rt(90)
    a1.fd(10)
    a1.color(cor1)
    a2.color(cor2)
    n = 4
    lado = 40
    for agente in [a1, a2]:
        for i in range(4):
            my_first_agent.polygon_generalizado(agente, n, lado)
            agente.penup()
            agente.fd(50)
            agente.pendown()


if __name__ == '__main__':
    mauro_oddo = turtle.Turtle()
    claudio = turtle.Turtle()
    c1 = 'red'
    c2 = 'blue'
    c3 = 'green'
    c4 = 'brown'
    desenho(mauro_oddo, claudio, c1, c2)
    mauro_oddo.fd(-20)
    claudio.rt(-90)
    claudio.fd(-20)
    desenho(claudio, mauro_oddo, c3, c4)
    turtle.mainloop()

    # Exemplo: tartarugas andando juntas
    mauro_oddo.color('red')
    claudio.color('blue')
    claudio.rt(90)
    claudio.fd(8)
    claudio.lt(90)
    for j in range(100):
        passo(mauro_oddo)
        passo(claudio)
