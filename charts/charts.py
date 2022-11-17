import matplotlib.pyplot as plt

def generate_graph():
    labels=['A','B','C','D']
    values=[200,300,100,200]

    fig, ax=plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()