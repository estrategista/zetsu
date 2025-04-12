
# ZETSU API INTERNA

## classificar_resposta(resposta: str) -> str
Classifica a resposta de uma API como:
- esperado
- falha
- risco
- oportunidade (futuramente)

## registrar_novo_teste(resposta: str, rotulo: str) -> None
Adiciona uma nova entrada ao dataset interno e treina novamente.

## interpretar_logs(path: str = "zetsu_logs.csv") -> str
Lê os logs e retorna uma interpretação simbólica da atividade registrada.
