# Projetos 3

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1145440299905200168/1156263713486147665/image-removebg-preview_VERMELHO_CERTO.png?ex=651455ff&is=6513047f&hm=4b9a61b213eef4e16bb236b503b9f9f05ac9ec05e9833b0bdce34b32161a7d35" alt="Logo do Eden">
</p>
<br></br>

# 🎥 Solução

Nossa solução, o LUMI, é inspirada no sobrenome dos Irmãos Lumière, os criadores do cinematógrafo e do cinema audiovisual. O LUMI foi desenvolvido com o objetivo de fornecer uma ferramenta de gestão que auxilie os colaboradores do Libreflix. Assim, independentemente da experiência na área da computação, os colaboradores poderão lidar com diversos problemas relacionados à divisão de papéis e à gestão de conteúdos. Além disso, o LUMI proporciona uma maior interação entre os usuários e colaboradores, oferecendo diversas funcionalidades que estão descritas abaixo.

Para mais detalhes da nossa solução e do nosso processo de desenvolvimento, veja no nosso <b>[Google Sites](https://sites.google.com/cesar.school/eden/equipe).</b>
<br></br>

# ⚙️ Funcionalidades

- <b>Gestão de Cargos dos Colaboradores:</b> É possível conceder diferente cargos a colaboradores que desejam auxiliar em partes do site.
- <b>Cargos dos Colaboradores:</b> Os cargos disponíveis são os de MasterUser, ReportUser e MidiaUser.
- <b>Status do Envio de Mídia:</b> Os formulários apresentam três estados (Em_Análise, Aprovado e Reprovado) para ajudar os usuários e colaboradores a terem um melhor controle do processo de aceitação
- <b>Histórico:</b> Os usuários serão capazes de verem no seu histórico oque assistiram recentemente e se terminaram de assistir.
- <b>Formulário de Reporte e Suporte:</b> Os usuários serão capazes de reportar problemas encontrados nos conteúdos da Libreflix. Também poderão entrar em contato com o time de suporte.
<br></br>

# 💾 Tecnologias Utilizadas

- <b>Ferramentas:</b> Python, HTML, CSS e JavaScript
- <b>Framework:</b> Django
- <b>IDE:</b> VS Code

<br>

# ☕ Usando LUMI
Para usar LUMI, siga estas etapas:<br>
<sub>***OBS.: A depender do seu sistema operacional, alguns dos comandos apresentados nessa descrição podem ser diferentes.***</sub>
### Instalando a Aplicação no seu Computador:

1. Crie uma pasta no seu computador, é ideal nomeá-la com o nome da aplicação, pois ela receberá o que está aqui no Github!
2. Com o botão direito do mouse, clique na pasta e selecione a opção "Abrir Terminal"
3. No terminal, copie e cole o seguinte comando e pressione enter
<dt> 
  
    git clone https://github.com/paulo-campos-57/Projetos3

</dt>

4. Após isso, abra uma IDE Python de sua preferência a pasta que recebeu os arquivos do LUMI nela
5. Agora, precisamos abrir o terminal da IDE dentro da pasta "eden_projects" mais externa. Clicando com o botão direito nela, selecione a opção "Abrir Terminal Integrado"

<br>

 ### Criando um Ambiente Virtual
6. Agora, precisamos criar um ambiente virtual para executarmos o LUMI. Utilize o comando indicado abaixo no terminal que abrimos no ponto 5. Quando o processo tiver terminado, uma nova pasta nomeada "venv" será criada no diretório atual.
<dt> 
  
    python -m venv venv

</dt>
7. Ative o ambiente virtual utilizando o comando abaixo. Será possível visualizar do lado direito de seu diretório atual o nome de seu ambiente virtual entre parênteses e verde.
<dt> 

    //Windows  
    venv/scripts/activate
    //Linux e MacOS
    source myenv/bin/activate
</dt>
8. Depois de ativar o ambiente, precisaremos instalar as dependências e bibliotecas necessárias para o funcionamento do LUMI. Utilize o comando abaixo:
<dt> 
  
    pip install -r requirements.txt

</dt>
9. Para criação e inicialização correta das tabelas do SQLite, utilizaremos os seguintes comandos separadamente:
<dt> 
  
    python manage.py makemigrations

</dt>
<dt> 
  
    python manage.py migrate

</dt>
<br>

### LUMI na WEB e interface Admin!
10. Usando o seguinte comando, podemos finalmente desfrutar do LUMI!
<dt> 
  
    python manage.py runserver

</dt>
<sub>***OBS2.: É importante lembrar que o LUMI atualmente funciona em hosts locais!***</sub>
<br>
<br>

- Caso deseje conferir o funcionamento do SQLite na interface oferecida pelo Django, siga próximo passo a passo a seguir

<br>

11. Clique com o botão esquerdo dentro do terminal onde o LUMI está sendo executado e pressione "ctrl+c" para parar a execução do site.
12. Utilize o comando a seguir para criar um usuário admin Django (este perfil é apenas local, utilizado comumente no Django para testes):
<dt> 
  
    python manage.py createsuperuser

</dt>
13. Será pedido que você insira um username, um email e a sua senha duas vezes. Quando todos esses passos tiverem sido atendidos, basta rodar o servidor novamente e no fim da url da página, colocar "/admin/" e pressionar enter. Você terá algo como "http://127.0.0.1:8000/admin/". Lá, utilize os dados cadastrados por você para criação do seu super usuário.


14. Para uso das funcionalidades, criamos o arquivo "setup_bd.py" que simula o acervo do Libreflix. Para que o SQLite seja alimentado com os dados, basta utilizar o comando:

<dt> 
  
    python setup_bd.py

</dt>


# 🤝 Equipe EDEN

Somos estudantes de ciência da computação e design do 3º período da instituição CESAR School. Escolhemos o nome "Eden" para homenagear o primeiro cinema do mundo, "The Eden Theatre", localizado em uma comuna francesa, La Ciotat, sendo o cinema mais antigo em funcionamento.
<br></br>

## 💻 Desenvolvedores:
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/paixaoao">
        <img src="https://avatars.githubusercontent.com/u/126728380?v=4" width="100px;" alt="Foto Paixas"/><br>
        <sub>
          <b>Arthur Paixão</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/EstelaLacerda">
        <img src="https://avatars.githubusercontent.com/u/117921412?v=4" width="100px;" alt="Foto Stora"/><br>
        <sub>
          <b>Estela Lacerda</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/MatheusGom">
        <img src="https://avatars.githubusercontent.com/u/117746778?v=4" width="100px;" alt="Foto Matheus Gomes"/><br>
        <sub>
          <b>Matheus Gomes</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/paulo-campos-57">
        <img src="https://avatars.githubusercontent.com/u/77108503?v=4" width="100px;" alt="Foto Megas"/><br>
        <sub>
          <b>Paulo Campos</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/SofiaValadares">
        <img src="https://avatars.githubusercontent.com/u/113111708?v=4" width="100px;" alt="Foto Sofia Valadares"/><br>
        <sub>
          <b>Sofia Valadares</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/virnaamaral">
        <img src="https://avatars.githubusercontent.com/u/116957619?v=4" width="100px;" alt="Foto Virnas"/><br>
        <sub>
          <b>Virna Amaral</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
<br></br>
