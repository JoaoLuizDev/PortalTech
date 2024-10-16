*Após uma varredura rápida no sistema de banco de dados de uma empresa de vendas, identificamos a necessidade de melhorar a segurança dessas 
informações. Por isso, será necessário desenvolver um novo banco para armazenar os dados mais importantes, como detalhes dos clientes, valores 
faturados diariamente e informações sobre os produtos, além de outros. Sendo assim, explique quais são os pilares da segurança de dados que 
devem ser seguidos para que o novo banco seja bem projetado e funcione corretamente.**

**Realize essa atividade no WORD ou no Bloco de Notas, suba esse arquivo para algum repositório e compartilhe o link no campo ao lado para que 
outros desenvolvedores possam analisá-lo.*



**Pilares da Segurança de Dados:**

- Confidencialidade:

**Controle de Acesso:** Implemente um sistema de controle de acesso baseado em funções para garantir que apenas pessoas autorizadas tenham acesso aos dados sensíveis. Use autenticação forte, como senhas complexas e autenticação de dois fatores (2FA).

**Criptografia:** Os dados devem ser criptografados em repouso (armazenamento) e em trânsito (comunicações) para evitar o acesso não autorizado.

**Máscara de Dados:** Em certos casos, é útil usar a máscara de dados para ocultar partes sensíveis dos dados, tornando-os ilegíveis para a maioria dos usuários.

- Integridade:

Controle de Versão: Mantenha um registro de versões dos dados para permitir a detecção de alterações não autorizadas ou corrupção de dados.

Validação de Dados: Implemente verificações de integridade nos dados para garantir que eles estejam sempre em um estado válido e consistente.

Checksums e Hashing: Use checksums ou funções de hash para verificar se os dados não foram alterados durante o armazenamento ou transmissão.

- Disponibilidade:

**Backup e Recuperação:** Mantenha backups regulares dos dados e estabeleça procedimentos de recuperação para lidar com desastres ou falhas de hardware.

**Tolerância a Falhas:** Projete o sistema de banco de dados de forma que seja resistente a falhas, com redundância de hardware, balanceamento de carga e planos de contingência.

**Monitoramento: ** Utilize ferramentas de monitoramento para rastrear o desempenho do sistema, bem como a disponibilidade dos recursos, e implemente alertas para problemas críticos.

- Autenticidade:

**Auditoria:** Mantenha registros de auditoria para rastrear quem acessa os dados, quando e quais ações foram realizadas. Isso ajuda a detectar e responsabilizar atividades maliciosas.

**Assinaturas Digitais:** Use assinaturas digitais para verificar a autenticidade dos dados e garantir que eles não tenham sido adulterados.

- Não-Repúdio:

**Assinaturas Digitais:** Além de garantir a autenticidade, as assinaturas digitais também garantem que uma pessoa não possa negar a autoria de uma ação ou transação.
Privacidade:

**Conformidade com Regulamentações:** Certifique-se de que o banco de dados esteja em conformidade com as regulamentações de privacidade de dados, como o Regulamento Geral de Proteção de Dados (GDPR) ou qualquer outra regulamentação aplicável em sua região.

**Anonimização de Dados:** Se possível, anonimize ou pseudonimize os dados pessoais para proteger a privacidade dos clientes.

- Segurança Física:

**Localização Segura:** Armazene os servidores e sistemas de banco de dados em locais físicos seguros com controle de acesso restrito.

**Proteção contra Roubo e Desastres:** Implemente medidas para proteger os dados contra roubo, incêndios, inundações e outros desastres físicos.

- Educação e Treinamento:

**Conscientização dos Funcionários:** Eduque os funcionários sobre práticas seguras de dados e os riscos de segurança, além de realizar treinamentos regulares de segurança.
Gerenciamento de Riscos:

**Avaliação de Riscos:** Realize avaliações regulares de riscos para identificar ameaças e vulnerabilidades, e desenvolva estratégias para mitigar esses riscos.
Certifique-se de que todos esses pilares sejam considerados ao projetar o novo banco de dados e que as melhores práticas de segurança de dados sejam seguidas para garantir a proteção adequada das informações sensíveis da empresa.
