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

*-> compras com quantity negativo serão tratadas separadamente*

*-> compras com price zero não serão consideradas (removidas)*

*-> compras cujos items não possuem description não serão consideradas (removidas)*

*-> compras cujo customer id é deconhecido não serão consideradas (removidas), já que não poderão ser identificados posteriormente*

*-> o atributo quantity negativo significa uma devolução do produto e consequentemente a empresa precisa reembolsar o cliente, o que implica que o atributo price também tenha um valor negativo*

*-> clientes que retornam mais produtos do que compram não serão considerados (removidos). Isso indica que o recorte temporal dos dados colhidos não conseguiu capturar as compras anteriores feitas por estes clientes*

*-> items cujo stock code possuem apenas caracteres alfabéticos (como W',  'CRUK',  'J',  'BL') parecem não possuir um produto relacionado. Estes itens não serão considerados nos cálculos do total de itens comprados por cliente*

*-> items com stock codes como 47566 e 47566B serão tratados como produtos diferentes*

*-> a unidade monetária utilizada foi o dólar americano*

*-> compras cujo invoice_no começam com a letra C indicam uma transação com quantity negativo, portanto serão tratadas isoladamente.

# **ESTRATÉGIA DA SOLUÇÃO**

![IoT-method](refereces/iot_method.png)

### Input

- **Business problem**: segmentar os clientes em grupos e encontrar aqueles mais valiosos.
- **Business questions**: descritos na seção anterior
- **Dados disponíveis**: dataset de transações que ocorreram entre Nov-2016 e Dec-2017.

### Output

- **Dashboard** com informações do grupo Insiders
- **Relatório** com as respostas para as seguintes perguntas de negócio:
* *Quem são as pessoas elegíveis para participar do programa de Insiders?*
* *Quantos clientes farão parte do grupo?*
* *Quais as principais características desses clientes?*
* *Qual a porcentagem de contribuição do faturamento, vinda do Insiders?*
* *Quais as condições para uma pessoa ser elegível ao Insiders?*
* *Quais as condições para uma pessoa ser removida do Insiders?*


### Tasks
- Quem são as pessoas elegíveis para participar do programa de Insiders? 
* O que significa ser elegível? Para a empresa, o que é exatamente um cliente valioso?
* Assumiremos que alto valor seja sinônimo de Lifetime Value (LTV)

- Quantos clientes farão parte do grupo??
* Determinar o cluster Insiders
* Contar quantos clientes estão no grupo e qual o percentual em relação ao número total de clientes

- Quais as principais características desses clientes?
* Determinar o cluster Insiders
* Descrever os clientes do grupo em termos dos valores médios dos atributos utilizados na clusterização

- Qual a porcentagem de contribuição do faturamento, vinda do Insiders??
* Determinar o cluster Insiders
* Calcular o faturamento acumulado obtido pelo grupo e dividir pelo faturamento total obtido pela base

- Quais as condições para uma pessoa ser elegível ao Insiders??
* Determinar o cluster Insiders
* Determinar o intervalo de confiança (de variação dos atributos) a ser considerado para elegibilidade e verificar o quão próximo da média do grupo está o comportamento do cliente

- What are the conditions for a person to be removed from the Insiders program?
* Determinar o cluster Insiders
* Determinar o intervalo de confiança (de variação dos atributos) a ser considerado para elegibilidade e verificar o quão longe da média do grupo está o comportamento do cliente


# **CICLO DO PROJETO**

![crisp-ds](references/crisp.png)

## Step 00. Settings
* Importação das bibliotecas, pacotes e funções necessárias.
* Carregamento e verificação dos dados disponíveis através de um arquivo CSV.

## Step 01. Data Description:
* Renomeção das colunas e verificação do tamanho do dataset (avaliar a necessidade de ferramentas para tratar grande volume de dados).
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
Prepare data so that the Machine Learning models can more easily learn and perform more accurately. Then create an embedded space for data.
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
Analyse clusters after Machine Learning modelling.
* Inspeção visual do espaço de dados montado por cada modelo
* Análise do profile (atributos) de cada cluster para cada modelo treinado
* Escolha do modelo final que apresenta a melhor performance

## Step 10. Exploratory Data Analysis for Business:
Test business hypotheses and answer business questions. 
* Criação e teste das hipóteses de negócio e elaboração das respostas para as perguntas de negócio 

## Step 11. Deploy to Production:
Plan deployment architecture and implement it.
* Planejamento e implementação da arquitetura de deploy do modelo
* Criação do banco de dados que será utilizado na solução do problema

# **TOP 3 INSIGHTS**

- **O grupo Insiders contribui com 30.33% do faturamento da empresa,** equivalente a $2,3 milhões
- **Em média, a receita gerada pelos clientes do grupo Insiders é 185x maior do que a receita gerada pelos clientes do cluster que gastam menos**
- **Em média, a frequência de compras do grupo Insiders é 14,36% e 117% maior do que a frequência de compras do segundo e terceiro grupos de clientes de melhor desempenho, respectivamente**

# **BUSINESS SOLUTION**

**A seguinte imgagem explica a arquitetura de deploy utilizada na solução deste problema**

![deployment-architecture](img/deployment_architecture.png)

**Confira o dashboard final elaborado para apresentar a solução do problema**

<--!http://insiders-project.herokuapp.com/public/dashboard/bf29cd43-922f-4a0c-bc2f-27d9d8336e29-->


# **CONCLUSÕES**

Problemas de clusterização são significativamente mais complexos de resolver, uma vez que a ausência de uma variável resposta, típica de problemas não-supervisionados, nos obriga a nos aprofundar mais no entendimento do negócio a fim de nos guiar na tomada de decisões de quais modelos implementar, quais features derivar e quais informações são realmente relevantes para o problema. A análise dos dados deixa de ser meramente matemática e estatística e demanda mais interpretação e intuição em relação ao negócio e o problema em questão.

# **LIÇÕES APRENDIDAS**

**Como desenvolver um projeto de data Science não supervisionado**

**Como utilizar as ferramentas da AWS (S3, EC2 and RDS), que oferecem uma plataforma de solução mais robusta para as empresas**

**Como criar um dashboard na ferramenta Metabse**

**Create an interim solution so as to give the business team something to work on until a more elaborate solution is delivered.**

**Como desenvolver soluções intermediárias e de melhorias graduais ao longo do projeto, entregando valor mais rapidamente ao time de negócios até apresentar a solução final robusta e melhor acabada.**

**Focar na resolução de problemas de negócios de forma mais essencial do que no uso de ferramentas**

**Compreender a importância decisiva do desenvolvimento cíclico de projetos e perceber qua a melhoria tanto de performance dos modelos quanto de resultados obtidos no negócio é gradualmente obtida à medida que mais ciclos são implementados**

# **PRÓXIMOS PASSOS**

**Streamlit**: criar uma página amigável no Streamlit que permita ao usuário fazer o upload dos dados via link, além de validar estes dados antes do envio ao bucket S3 hospedado pela AWS.

**Dashboard**: conversar com o time de negócio a fim de conhecer as informações mais relevantes a serem apresentadas.

**Embeddings**: testar outros embeddings que facilitem o agrupamento feito pelos modelos de ML

**Machine Learning Models**: testar mais modelos de ML a fim de obter melhores resultados. 

**Hypothesis**: elaborar e validar mais hipóteses de negócio a fim de aprofundar o entendimento do problema.

**Code**: revisar e reescrever o código a fim de melhorar a clareza na leitura, como também diminuir o consumo de recursos computacionais.


# LICENSE

# All Rights Reserved - Comunidade DS 2021

