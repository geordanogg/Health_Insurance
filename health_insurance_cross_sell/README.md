# **ENTENDIMENTO DO NEGÓCIO**

## **QUAL É A EMPRESA?**

Insurance All

## **QUAL É O MODELO DE NEGÓCIO?**

A Insurance All é uma empresa que fornece seguro de saúde para seus clientes, cujo modelo de negócio se dá da seguinte forma:

A seguradora exige um pagamento (denominado “prêmio anual”) do cliente para garantir indenizações em caso de doenças, tratamentos de saúde e quaisquer outras condições especificadas no contrato.

Assumindo que o prêmio custe $5.000 e a garantia seja de até $100.000, o cliente tem a garantia de que, por exemplo, se necessitar de um tratamento de saúde de $20.000, a seguradora o pagará (dado que é menor que o limite coberto pela garantia).

A lógica do negócio consiste em faturar com uma base enorme de clientes, milhares deles, que pagam pela garantia, mas de fato não chegam a usá-la integralmente. A empresa se vale de conhecimentos estatísticos e análises de riscos que garantem que na maioria dos casos os clientes irão demandar menos do que tem direito, onde reside o lucro da operação.

## **QUAL É O PROBLEMA DE NEGÓCIO?**

A equipe de produtos da Insurance All está analisando a possibilidade de oferecer um novo produto, o seguro de automóveis, para seus clientes que já possuem seguro de saúde.

Assim como o seguro de saúde, os clientes desse novo plano de seguro de automóveis precisam pagar um valor anualmente à Insurance All para obter um valor assegurado pela empresa, destinado aos custos de um eventual acidente ou dano ao veículo.

Ano passado, a Insurance All fez uma pesquisa com cerca de 380 mil clientes sobre o interesse em aderir a este novo produto. Todos os clientes responderam a esta pesquisa e demonstraram interesse ou não em adquirir o seguro de automóvel, ficando essas respostas salvas em um banco de dados junto com outros atributos dos clientes.

O time de produtos selecionou 127 mil novos clientes, que não responderam à pesquisa, para participar de uma campanha na qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pelo time de vendas através de ligações telefônicas. Contudo, o time de vendas tem uma capacidade de realizar apenas 20 mil ligações dentro do período da campanha.

# **ENTENDIMENTO DO PROBLEMA**

## **QUAL O DESAFIO QUE ESTE PROJETO VISA SUPERAR?**

Nesse contexto, a empresa contratou um consultor de Ciência de Dados para construir um modelo que prediz se o cliente estaria ou não interessado no seguro de automóvel.

Com a esta solução, o time de vendas espera conseguir priorizar as pessoas com maior interesse no novo produto e assim, otimizar a campanha realizando apenas contatos aos clientes mais propensos a realizar a compra.

Como resultado desta consultoria, é necessário entregar um relatório contendo algumas análises e respostas às seguintes perguntas:

* Principais Insights sobre os atributos mais relevantes de clientes interessados em adquirir um seguro de automóvel.
* Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar fazendo 20.000 ligações?
* E se a capacidade do time de vendas aumentar para 40.000 ligações, qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar?
* Quantas ligações o time de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro de automóvel?

**Referências:**

https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction/metadata

https://sejaumdatascientist.com/como-usar-data-science-para-fazer-a-empresa-vender-mais/


# **BUSINESS ASSUMPTIONS**

**HYPOTHESIS**

De acordo com as informações do banco de dados, **Annual_Premium** é o valor que o cliente precisa pagar anualmente para ter a cobertura do seguro de saúde. Não se refere portanto à oferta do seguro de automóvel

Com base em uma pesquisa nas referências abaixo, o **custo médio do seguro de automóveis** foi considerado $ 1.000 por ano. Como a maioria das referências abaixo das estimativas são mais altas, as estimativas de receita para este projeto são um tanto pessimistas.

Eu assumi que **10%** dos interessados irão aceitar a oferta do novo seguro depois de serem contactados.

References:

https://www.bankrate.com/insurance/car/average-cost-of-car-insurance/

https://www.policygenius.com/auto-insurance/learn/how-much-is-car-insurance/

https://www.businessinsider.com/personal-finance/average-cost-of-car-insurance


# **ESTRATÉGIA DA SOLUÇÃO**

![IoT-method](references/iot_method.png)

### Input

- **Business problem**: ordenar os novos clientes pela propensão de aceitar a oferta do novo seguro
- **Business questions**: descritos na seção anterior
- **Dados disponíveis**: dataset com dados de 380 mil clientes que já responderam á pesquisa de interesse

### Output

- **Planilha Online** que calcula o score de propensão de compra para uma lista de clientes inputadas pelo usuário
- **Relatório** com as respostas para as seguintes perguntas de negócio:
* *Principais Insights sobre os atributos mais relevantes de clientes interessados em adquirir um seguro de automóvel.*
* *Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar fazendo 20.000 ligações?*
* *E se a capacidade do time de vendas aumentar para 40.000 ligações, qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar?*
* *Quantas ligações o time de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro de automóvel?*


### Tasks
> Quais são os atributos mais relevantes de clientes interessados em adquirir um seguro de automóvel?
* Estimar a relevância de todos os atributos através de alguns métodos de seleção de features

> Qual percentual de clientes interessados será atingido após 20 mil ligações?
* Ordenar os clientes pela propensão de compra
* Observar a métrica de *Recall at K* para a posição 20 mil

> Qual percentual de clientes interessados será atingido após 40 mil ligações?
* Ordenar os clientes pela propensão de compra
* Observar a métrica de *Recall at K* para a posição 40 mil

> Quantas ligações são necessárias para atingir 80% do total de clientes interessados?
* Determinar o cluster Insiders
* Observar a métrica de *Recall at K* para o valor 0.80 e retornar o valor de K


# **CICLO DO PROJETO**

![crisp-ds](references/crisp.png)

## Step 00. Settings
* Importação das bibliotecas, pacotes e funções necessárias.
* Carregamento e verificação dos dados disponíveis através de um arquivo CSV.

## Step 01. Data Description:
* Renomeação das colunas e verificação do tamanho do dataset (avaliar a necessidade de ferramentas para tratar grande volume de dados).
* Verificação dos tipos de dados em cada coluna e mudanças de tipo que se façam necessárias para melhor tratamento pelos algoritmos posteriormente
* Verificação de dados faltantes e decisão de como tratá-los (remoção, reamostragem artificial, inviabilidade da solução)
* Breve descrição estatística dos atributos numéricos e categóricos a fim de detectar anomalias que fogem do escopo do problema, bem como a presença de possíveis outliers que irão impactar a performance dos algoritmos posteriormente.

## Step 02. Data Filtering:
* Filtragem de linhas e deleção de colunas que não contém informações relevantes para a modelagem ou não ajudam a resolver o problema.

## Step 03. Feature Engineering:
Criação de variáveis (features) relevantes para a resolução do problema

## Step 04. Exploratory Data Analysis:
* Análise isolada de cada feature e sua realação com as demais.
* Exploração dos dados a fim de obter uma intuição da distribuição dos mesmos no espaço de dados (exploração de embedding).

## Step 05. Data Preparation:
* Preparação dos dados a fim de ajudar os modelos de machine learning a aprenderem e performarem com maior acurácia.
* Seleção do espaço de embedding mais adequado ao problema

## Step 06. Feature Selection:
* Seleção das features mais relevantes para treinar os modelos.

## Step 07. Hyperparameter Fine Tuning:
* Teste de diferentes modelos de machine learning e seleção daquele que apresenta a melhor performance baseado nas métricas escolhidas (silhouette score)
* Escolha dos melhores valores para cada parâmetro dos modelos testados que maximizam a performance

## Step 08. Model Training:
* Treino dos modelos com os melhores parâmetros encontrados e medição da sua performance

## Step 09. Cluster Analysis
* Inspeção visual do espaço de dados montado por cada modelo
* Análise do profile (atributos) de cada cluster para cada modelo treinado
* Escolha do modelo final que apresenta a melhor performance

## Step 10. Exploratory Data Analysis for Business:
* Criação e teste das hipóteses de negócio e elaboração das respostas para as perguntas de negócio

## Step 11. Deploy to Production:
* Planejamento e implementação da arquitetura de deploy do modelo
* Criação do banco de dados que será utilizado na solução do problema

# **TOP 3 INSIGHTS**

## - H2 - Clientes com carros novos/seminovos (menor que 2 anos), tem mais interesse em seguro de veículos.

> Falsa: Entre os interessados em adquirir o seguro de carro, quase 75% possuem carros seminovos. Apesar disso, entre os que possuem carros mais velhos o percentual de interesse é de quase 30%, enquanto entre os que possuem carros novos e seminovos o percentual de interesse é de apenas 5% e 17%, respectivamente.

![h2_hypothesis](references/h2_hypothesis.png)

**Sugestão**: depois da lista final de ligações a serem feitas, priorizar os clientes com veículos mais antigos.

## - H8 - Apenas 10 canais de venda concentram mais de 80% dos clientes que estão interessados em adquirir seguro de veículos.

> Verdadeira: Entre os 155 canais de venda catalogados na base, em apenas 10 deles estão concentrados 42780 clientes interessados em adquirir o seguro de carro, o que representa mais de 90% do total de clientes interessados. Além disso, há 34 canais de vendas pelos quais nenhum cliente demonstrou interesse em adquirir o novo produto.

![h8_hypothesis](references/h8_hypothesis.png)

**Sugestão:** depois da lista final de ligações a serem feitas, investigar os 3 canais com maior número de clientes.

## - H9 - Apenas 10 regiões concentram mais de 80% dos clientes que estão interessados em adquirir seguro de veículos.

> Falsa: Entre os 53 region_code catalogados na base, no Top-10 estão concentrados 33740 clientes interessados em adquirir o seguro de carro, o que representa cerca de 72% do total de clientes interessados. Com exceção da região de código 28, que sozinha representa quase 43% da base de interessados, nas demais regiões o percentual de interesse é mais uniforme.

![h9_hypothesis](references/h9_hypothesis.png)


# **BUSINESS RESULTS**

## Quais são os atributos mais relevantes de clientes interessados em adquirir um seguro de automóvel?

![attributes](references/results_attributes.png)

## Qual percentual de clientes interessados será atingido após 20 mil ligações?
* k=20000 ligações representa 26.24% da base de clientes
* Com esta quantidade de ligações é possível atingir cerca de 71.00% dos interessados

![20k_question](references/results_20k.png)

## Qual percentual de clientes interessados será atingido após 40 mil ligações?
* k=40000 ligações representa 52.48% da base de clientes
* Com esta quantidade de ligações é possível atingir cerca de 99.44% dos interessados

![40k_question](references/results_40k.png)

## Quantas ligações são necessárias para atingir 80% do total de clientes interessados?
* k=23601 ligações representa 30.96% da base de clientes
* Com esta quantidade de ligações é possível atingir cerca de 80.00% dos interessados

![80p_question](references/results_80p.png)

## Compilado dos Resultados de Negócio

<!--- [//]: <> (![compiled](references/results_compiled.png) ) -->

| Ligações  |  Random  |  Modelo  |  Ganho$  |
| --------- | -------- | -------- | ------- |
|  **20.000** |  5.25 milhões | **14.2** milhões | **2.7**x |
|  **23.601** |  7.30 milhões | **18.8** milhões | **2.6**x |
|  **40.000** |  21 milhões | **39.7** milhões | **1.9**x |

# - RANDOM MODEL vs ML MODEL

![random_vs_ml](references/results_random_model.png)

# **BUSINESS SOLUTION**

**A seguinte imgagem explica a arquitetura de deploy utilizada na solução deste problema**

![deployment](references/deploy_insurance.png)

**Google Sheet**

Uma Planilha Google foi criada para que a equipe de vendas possa verificar facilmente a probabilidade de um cliente se interessar pelo seguro de automóvel. Com esta solução, a equipe de vendas pode simplesmente inserir os dados dos clientes e com apenas um clique obter a probabilidade de cada um demonstrar interesse na aquisição do novo seguro, podendo optar por fazer contato primeiro com aqueles que apresentam o maior *score*.

**Confira a planilha final elaborada para apresentar a solução do problema**

[//]: # (https://docs.google.com/spreadsheets/d/1fuRS5EtYqtX-nkf0gh-01Ltv6HowKl3gJbnzjlFIVUE/edit#gid=0)
![deployment](references/google_sheet.png)



# **CONCLUSÕES**

O particular problema de classificação conhecido como **Learning to rank** leva em conta algumas métricas especiais não muito usuais em típicos casos de mera determinação de qual classe pertence um determinado dado. As métricas de ranqueamento devem ser observadas com mais atenção, visto que impactam significativamente os resultados de negócios obtidos com os modelos treinados.

Neste problema em especial a priorização da métrica de Recall at K se deu pelo importante motivo de tentar reduzir a quantidade de oportunidades de negócio que poderiam ser perdidas caso o modelo deixasse de recomendar clientes potencialmente interessados (os casos de falsos negativos onde ele deixaria passar os clientes interessados). O impacto financeiro positivo será muito maior se reduzirmos os casos de falsos negativos do que os falsos positivos, pois neste último caso o prejuízo seria apenas de uma ligação perdida, e no primeiro caso, uma grande oportunidade real de negócio perdida.

# **LIÇÕES APRENDIDAS**

**Como construir uma API usando Flask e hospedar no Heroku Cloud, a fim de que uma planilha possa fazer as requisições de predição usando poucos cliques**

**Como criar um script para automatizar rotinas dentro de uma planilha no Google Sheets**

**Como desenvolver soluções intermediárias e de melhorias graduais ao longo do projeto, entregando valor mais rapidamente ao time de negócios até apresentar a solução final robusta e melhor acabada.**

**Focar na resolução de problemas de negócios de forma mais essencial do que no uso de ferramentas**

**Compreender a importância decisiva do desenvolvimento cíclico de projetos e perceber qua a melhoria tanto de performance dos modelos quanto de resultados obtidos no negócio é gradualmente obtida à medida que mais ciclos são implementados**


# **PRÓXIMOS PASSOS**

**Hypothesis**: elaborar e validar mais hipóteses de negócio a fim de aprofundar o entendimento do problema.

**Code**: revisar e reescrever o código a fim de melhorar a clareza na leitura, como também diminuir o consumo de recursos computacionais.

**Google sheet**: aperfeiçoar a interface e fazer validação de dados de entrada pelo usuário.

**Features**: melhorar o desempenho dos modelos com a criação de novas features e combinações delas que sejam mais relevantes para os algoritmos e também façam sentido para o negócio.

**API**: aperfeiçoar a interface entre API e planilha reportando mensagens mais intuitivas de possíveis erros aos usuários.



# LICENSE

# All Rights Reserved - Comunidade DS 2021
