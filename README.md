# 🩺 Sistema de Gestão Médica

Sistema web desenvolvido para facilitar o gerenciamento de clínicas e consultórios médicos. A aplicação permite o controle eficiente de pacientes, médicos, especialidades, agendamentos e muito mais — tudo com uma interface amigável e acessível.

## 🚀 Funcionalidades

- Cadastro e gerenciamento de **pacientes**, **médicos** e **especialidades**
- Agendamento de consultas com data e horário
- Visualização de consultas marcadas
- Relatórios de atendimentos
- Controle de status das consultas
- Interface intuitiva e responsiva com Bootstrap

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework Web:** Django
- **Frontend:** Bootstrap 5
- **Banco de Dados:** PostgreSQL
- **Template Engine:** Django Templates

## 📸 Imagens do Sistema



## ⚙️ Como Executar o Projeto

```bash
# 1. Clone o repositório:
git clone https://github.com/CelsoSReis/med.git
cd med

# 2. Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. Instale as dependências:
pip install -r requirements.txt

# 4. Configure o banco de dados no settings.py

# 5. Aplique as migrações:
python manage.py migrate

# 6. Crie um superusuário:
python manage.py createsuperuser

# 7. Inicie o servidor:
python manage.py runserver
