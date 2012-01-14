# -*- coding:utf-8 -*-

from django.db import models

class Subscription(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    email = models.EmailField('E-mail', unique=True)
    phone = models.CharField('Telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    paid = models.BooleanField('Pago')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "subscription"
        ordering = ["created_at"]
        verbose_name = u"Inscrição"
        verbose_name_plural = u"Inscrições"


# FUNCAO DA DOCUMENTAÇÃO DO SOUTH ***
def documentacao_south():
    '''

*** O South acrescenta os seguintes comandos a mais no manage.py:
    Para executa-los siga o exemplo: python manage.py convert_to_south <nome_da_app> <parametros>
    Pode se usar o parametro --help para ajuda.

    *** convert_to_south: converte uma app para a o tipo do south, coloca ela sob a visibilidade do south
        ou seja, a partir de agora o south monitora a app informada.

    *** datamigration: cria migrações de dados.
        Muda os dados do banco (diferente do schemamigrantion).
        Exemplo:
            se você quer mudar o tipo de uma coluna, e esta coluna ja tem muitos dados cadastrados,
            você pode ter que dizer como traduzir da coluna antiga para a coluna nova, se for simples.
        Exemplo_2:
            você está criando um model novo, e quer passar de um model para outro, então voce pega o
            datamigration e pode criar um processo especifico para migrar de um modelo antigo para um
            modelo novo. Então é você faz um pipeline de como pegar os dados da estratégia antiga e
            coloca na nova.

    *** graphmigrations: pega todas as migrações do seu projeto e cria um grafo demonstrando a dependencia
        e sequencia de cada migração.
        Exemplo:
            $ python manage.py graphmigrations
            digraph G {
            "subscription.0001_initial" -> "subscription.0002_auto__add_field_subscription_paid"
            }

    *** migrate: executa a migração, é um processo a mais ao processo de syncdb.


    *** schemamigration: cria migração de esquema, que são mudanças nas tabelas em si.
        Muda o esquema do banco.
        Você cria uma migração de dados para não misturar com a migração de esquema

    *** syncdb: o syncdb original do django somente faz o processo de validar, pega o que você tem
        nos models e converte para tabelas no banco (somente preenche o que não tem).
        Já o syncdb do South sobrepoe o do django e funciona somente para as apps que não são
        manipuladas pelo South, para não estragar as apps que são monitoradas pelo south


*** USANDO O SOUTH:

    *** MIGRAÇÃO INICIAL -- EXECUTAR QUANDO FOR MIGRAR PELA PRIMEIRA VEZ UMA APP DO DJANGO
        RECOMENDO EXECUTAR ASSIM QUE CRIAR O MODEL.
        1 - no diretório raiz do projeto execute o comando:
            $ python manage.py schemamigration subscription --initial --stdout
            --initial cria a migração inicial, que equivale a dizer pro south o estado
            --stdout mostra na tela o conteudo do arquivo 0001_initial.py
            original dos models daquela app, e ele grava no arquivo "0001_initial" dentro da
            pasta migrantions dentro da sua app.
            Deixando a árvore assim:

    *** MIGRANDO ALTERAÇÃO -- SÓ DEPOIS DE TER FEITO A MIGRAÇÃO INÍCIAL:
        1 - no diretório raiz do projeto execute o comando:
            $ python manage.py schemamigration subscription --auto -v2
            --auto serve para que o processo seja automatico
            --v2 mostra todo o processo com o maximo de detalhamento na tela
        2 - ele vai buscar por todas as alterações em models no app subscripton e salva-las em
            um arquivo "0002_auto__add_field_subscription_paid.py" contendo o estado anterior
            model e a alteração que foi feita. ATENÇÃO: o que vem depois do "0002_" refere-se
            aos parametros usados no comando schememigration e a alteração de fato realizada
            no model e o número 2 representa a versão e vai sendo incrementado a cada
            schememigration seguido por um migrate.
        3 - Executar o comando: $ python manage.py migrate subscription
            Ele vai buscar todas as alterações do model dentro do arquivo 0002... e alterar
            efetivamente a tabela referente no banco de dados. Também salva um registro na
            tabela "south_migrationhistory" representando esta migração realizada.

    *** USANDO O CONVERT_TO_SOUTH --
        O convert_to_south avisa o south que
            cria o migration initial (aquele arquivo 0001_initial), mas não aplica no banco,
            por que ja tem essa tabela la no banco pra não dar erro, dizendo pro south que
            esta app ja está em seu estado inicial.

    '''
