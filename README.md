# Atividade Prática de CI/CD

## Evidência Adicional

**1. O que representa a etapa de CI neste projeto?**
Representa a Integração Contínua, que é o processo automatizado responsável por baixar o código, preparar o ambiente Python e executar os testes automatizados a cada alteração enviada ao repositório.

**2. O que impede a execução do Continuous Delivery quando existe um defeito?**
A execução é impedida pela dependência `needs: ci` configurada no job de Delivery, atuando em conjunto com a falha na etapa de testes. Se algum teste encontrar um defeito e falhar no job de CI, o pipeline é interrompido imediatamente e o job de Delivery nem chega a ser iniciado.

**3. Qual seria a próxima etapa necessária para transformar este pipeline em Continuous Deployment?**
Seria necessário adicionar um novo job de Deploy logo após a etapa de Delivery. Esse novo job conteria as credenciais de um servidor e os comandos de implantação para publicar a aplicação automaticamente no ambiente de produção, sem qualquer necessidade de aprovação manual.
