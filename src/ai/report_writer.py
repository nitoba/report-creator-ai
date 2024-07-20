from crewai import Task

from src.ai.agent import report_writer

writer = Task(
    description="""Use os dados fornecidos pelo usuário para escrever um relatório semanal.
    Escreva um relatório semanal detalhado que aborde os seguintes pontos principais:
        1. Resumo das atividades da semana.
        2. Principais realizações e marcos atingidos.
        3. Desafios enfrentados e como foram superados.
        4. Metas para a próxima semana se houver.
        5. Observações adicionais se houver.

    Formato:
        Reporte Semanal IBS - (Data do primeiro registro começando com Standup) à (Data do útilmo registro começando com Standup)

        1. Resumo das Atividades da Semana:
        - Descreva brevemente as atividades realizadas durante a semana.
        - Inclua datas e participantes relevantes.

        2. Principais Realizações e Marcos Atingidos:
        - Liste as principais realizações.
        - Explique por que esses marcos são importantes.

        3. Desafios Enfrentados e Como Foram Superados:
        - Identifique os principais desafios.
        - Descreva as soluções implementadas para superar esses desafios.

        4. Metas para a Próxima Semana:
        - Defina as metas e objetivos para a próxima semana.
        - Explique como essas metas se alinham com os objetivos de longo prazo.

        5. Observações Adicionais:
        - Adicione quaisquer comentários ou informações adicionais que sejam relevantes para o contexto do relatório.

    Dados fornecido pelo usuário:
    ---
    {report}
    ---

    Retorne o conteúdo gerado em português do Brasil se atentando para erros de grámatica.
    Se a linha do texto passar de 90 caracteres deve ser quebrada para próxima.
    Sempre que houver o nome 'Bruno' pode tratar como primeira pessoa, pois é quem deve ser
    referenciado como dono do relatório.
    Um novo registro a partir dos dados fornecidos sempre comecam com: Standup (DD/MM/YYYY),
    considere essa parte como data em que o registro foi criado para mostrar a data do título
    do relatório. Observe que o nome Standup não é incluso como data, apenas use como referência
    para conseguir se localizar as datas em que os registro foram criados.

    O Tom e o estilo do texto devem ser:
        - Mantenha um tom profissional e objetivo.
        - Utilize linguagem clara e direta.
        - Evite jargões técnicos, a menos que sejam essenciais.
        - Escreva em primeira pessoa. Ex: Realizei atividades..., participei de reuniões... etc.

    Não devolva nenhuma resposta além do conteúdo do relatório gerado conforme
    pedido acima, agracedimentos ou saudações finais não são necessários,
    apenas a geração do relatório.
    """,
    agent=report_writer,
    expected_output='Um relatório semanal detalhado que seja escrito com sucesso.',
)
