import { ReportCreatorStreamService } from '@/services/report-creator-stream.service'
import { useCallback, useRef, useState } from 'react'

const reportCreatorStreamService = new ReportCreatorStreamService()

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const fakeReport = `
**Relatório Semanal IBS - 25/07/2024 à 31/07/2024**

**1. Resumo das Atividades da Semana:**

Durante a semana de 25 a 31 de julho, realizei várias atividades importantes para o projeto Agrotrace. Iniciei trabalhos em cinco tarefas principais e finalizei outras quatro. Além disso, participei de reuniões com meus colegas de equipe para discutir os progressos e superar desafios.

**25/07/2024**

* Finalizei a tarefa #5601, corrigindo um problema que ocorria quando o número de produtor/propriedade era diferente da Timeline.
* Iniciei as tarefas #5581 (Integração/Setup Banco de dados vetorial no AgrotraceIA) e #5586 (Dashboard culturas).
* Participou de uma reunião com Thielson para discutir problemas de formulário no CMS e gráficos de perda do horta.

**26/07/2024**

* Continuou trabalhando na tarefa #5586, adicionando gráfico de perda e refazendo consultas na procedure.
* Participou de uma reunião com Ronaldo para discutir dificuldade na consulta por SQL usando agrupamentos.
* Participou de outra reunião com Iohan sobre gráficos de perda.

**29/07/2024**

* Finalizei a tarefa #5586, incluindo refazendo gráfico de Produtividade Média e Situação das Colheitas.
* Iniciei as tarefas #5661 (Filtros Atrasado - Evolução) e #5662 (Ajuste Modal - Evolução).
* Participou de uma reunião com Ronaldo e Iohan sobre adição da informação de atraso na sidebar da timeline.

**30/07/2024**

* Finalizei as tarefas #5652, #5661 e #5634.
* Iniciei a tarefa #5651 (Login dinâmico e temas).
* Participou de uma reunião com Iohan sobre validação de informação de atraso na timeline.

**31/07/2024**

* Finalizei as tarefas #5651, #5666, #5649 e #5683.
* Continuou trabalhando na tarefa #5479 (Identidade PEC), implementando novo design de login e fluxo de autenticação.

**2. Atividades Realizadas:**

Realizei várias atividades importantes durante a semana, incluindo:

* Corrigir problemas técnicos no Agrotrace
* Desenvolver novas funcionalidades para o Dashboard culturas
* Refazer consultas na procedure para melhorar desempenho
* Implementar novo design de login e flux
`

export function useReportStreaming() {
  const [isGeneratingReport, setIsGeneratingReport] = useState(false)
  const [streamedContent, setStreamedContent] = useState('')
  const [finishedStreaming, setFinishedStreaming] = useState(false)
  const abortReportCreation = useRef<() => void>()
  const titleInputRef = useRef<HTMLInputElement>(null)

  function handleReset() {
    setIsGeneratingReport(false)
    setStreamedContent('')
    setFinishedStreaming(false)
    abortReportCreation.current = undefined
  }

  const handleGenerateReport = useCallback(async () => {
    handleReset()
    setIsGeneratingReport(true)
    const result = await reportCreatorStreamService.execute()

    if (!result) {
      setIsGeneratingReport(false)
      return
    }

    abortReportCreation.current = result.abort

    for await (const data of result.stream) {
      if (data.isDone) {
        setFinishedStreaming(true)
        break
      }
      setStreamedContent((prev) => prev + data.data)
      setIsGeneratingReport(false)
    }
  }, [])

  const handleAbortReportCreation = useCallback(() => {
    titleInputRef.current!.value = ''

    if (abortReportCreation.current) {
      abortReportCreation.current()
      setFinishedStreaming(true)
    }
  }, [])

  return {
    isGeneratingReport,
    streamedContent,
    finishedStreaming,
    titleInputRef,
    handleGenerateReport,
    handleAbortReportCreation,
    handleReset,
  }
}
