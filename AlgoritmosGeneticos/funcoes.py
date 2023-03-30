import random

def funcao_objetivo_caixa_binaria(individuo):
    """ Computa a função objetivo no problema das caixas binárias.
    
    Args: 
        Individuo: lista contendo os genes das caixas binárias.
    Return:
    Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo) + 1

def individuo_caixa_binaria(n):
    """Gera um indíviduo para o problema das caixas binárias.
    
    Args:
        n: número de genes do indivíduo
    
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_caixa_binaria()
        individuo.append(gene)
    return individuo

def gene_letra(letras):
    """Sorteia uma letra.
    Args:
      letras: letras possíveis de serem sorteadas.
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra

def gene_caixa_binaria():
    """Gera um gene válido para o problema das caixas binárias
    
    Return:
        Um valor zero ou um
    """
    lista = [0,1]
    gene = random.choice(lista)
    
    return gene

def gene_cnb(valor_max_caixa):
    '''Gera um gene válido para o problema das caixas não binárias
    
    Args:
        valor_max_caixa: Valor máximo que a caixa pode assumir
        
    Returns:
        Um valor de 0 a 'valor_max_caixa' (incluso)
    '''
    
    gene = random.randint(0, valor_max_caixa)
    
    return gene

def individuo_cnb(numero_genes, valor_max_caixa):
    '''Gera um indivíduo válido para o problema das caixas não binárias
    
    Args:
        numero_genes: numero de genes na lista que representa o invíduo
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Returns:
        Uma lista que representa um indivíduo válido para o problema
    '''
    individuo = []
    
    for _ in range(numero_genes):
        
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    
    return individuo
    
def populacao_cnb(tamanho_populacao, numero_genes, valor_max_caixa):
    '''Cria uma população para o problema das caixas não-binárias
    
    Args:
        tamanho_população: número de indivíduos
        numero_genes: número de genes
        valor_max_caixa: valor maximo que a caixa pode assumir
    
    Returns:
        uma lista em que cada item é um indíviduo
    '''
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
    
    return populacao

def funcao_objetivo_cnb(individuo):
    '''Calcula o fitness do individuo para o problema das caixas não-binárias
    
    Args:
    
        individuo: lista que representa um individuo dentro do problema das CNB
    
    Returns:
        Um valor que representa o fitness do indiviuo
    '''
    fitness = sum(individuo)
    return fitness

def funcao_objetivo_pop_cnb(populacao):
    '''Calcula o fitness da populacao completa
    Args:
        populacao: lista com todos os individuos da população
        
    Returns:
        Uma lista com o fitness de cada individuo em ordem
    '''
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop

def mutacao_cnb(individuo, valor_max_caixa):
    '''Realiza a mutação do indivíduo
    
    Args:
        individuo: individuo que deve sofrer a mutação
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Returns:
        individuo que sofreu mutação
    '''
    gene_a_ser_mutado = random.randint(0,len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo

def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo
    
def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fitness
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados

def populacao_cb(tamanho,n):
    """Cria uma populaçãp no problema das caixas binárias.
    
    Args:
        tamanho: tamanho da população
        n_genes: número de genes
    
    Returns:
        Uma lista onde cada item é um indivíduo. Um invíduo é uma lista com n genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_caixa_binaria(n))
    
    return populacao

def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato

def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha
    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao

def selecao_roleta_max(populacao, fitness):
    """Seleciona indivíduos de uma população usando o método da roleta.
    
    Nota: Funciona apenas para problemas de maximização
    
    Args: população: 
        lista com todos os indivíduos da população
        fitness: valor da função objetivo dos indivíduos da população
    
    Returns: 
        População dos indivíduos selecionados
    
    """
    populacao_selecionada = random.choices(populacao, weights=fitness,           k=len(populacao))
    
    return populacao_selecionada
    
def funcao_objetivo_pop_cb(populacao):
    """Calcula a função objetivo para todos os membros de uma população
    
    Args:
        população: lista com todos os indivíduos da população
        
    Returns:
        Lista de valores representando a fitness de cada individuo da população.
    """
    
    fitness =[]
    for individuo in populacao:
        fobj = funcao_objetivo_caixa_binaria(individuo)
        fitness.append(fobj)
        
    return fitness

def cruzamento_ponto_simples(mae,pai):
    """Operador de cruzamento de ponto simples.
    
    Args:
        pai: uma lista representando um indivíduo
        mae: uma lista representando um indivíduo 
    
    Returns:
        Duas listas, sendo que cada uma representa um filhos dos pais que foram os argumentos.
    """
    ponto_de_corte = random.randint(1, len(mae)-1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + mae[ponto_de_corte:]
    
    return filho1, filho2

def mutacao_cb(individuo):
    """Realiza a mutação em um gene no problema das caixas binárias.
    
    Arg:
        Individuo: uma lista representando um individuo no problema das caixas binárias
        
    Return:
        Um indivíduo com um gene mutado.
    """
    
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_caixa_binaria()
    return individuo

def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca

def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado
