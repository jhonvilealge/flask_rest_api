# API REST em Flask com SQLAlchemy e Marshmallow



## Requisitos

Softwares requeridos pelo projeto

- [Python](https://www.python.org/)



## Configurando o ambiente

**Execute os comandos abaixo para rodar a aplicação**
```sh
# Realiza a instalação do gerenciador de dependências
$ pip3 install pipenv

# Cria ambiente virtual e faz a instalação das dependências do projeto
$ pipenv shell
$ pipenv install

# Cria o banco de dados temporário na raiz do projeto
$ flask db init
$ flask db migrate
$ flask db upgrade

# Caso ocorra algum erro ao fazer a migração do banco de dados temporário, execute os comandos abaixo
$ pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy flask-migrate
$ flask db init
$ flask db migrate
$ flask db upgrade

# Iniciar servidor
$ python server.py
```



## Endpoints

### Listar todos os alunos

**Request**

`GET /api/student`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": [
        {
            "course": "Psicologia",
            "cpf": "841.817.060-36",
            "created_on": "2021-01-29T19:26:43.551458",
            "email": "jsnow@gmail.com",
            "name": "Jon Snow",
            "phone": "(69) 99791-4811",
            "student_id": 1
        },
        {
            "course": "Relações Internacionais",
            "cpf": "084.596.719-33",
            "created_on": "2021-01-29T19:26:43.551458",
            "email": "daetarg@gmail.com",
            "name": "Daenerys Targaryen",
            "phone": "(68) 98780-2210",
            "student_id": 2
        },
        {
            "course": "Pedagogia",
            "cpf": "532.267.677-55",
            "created_on": "2021-01-29T19:26:43.551458",
            "email": "cerseilan@gmail.com",
            "name": "Cersei Lannister",
            "phone": "(84) 98129-7235",
            "student_id": 3
        }
    ],
    "message": "successfully fetched"
}
```

- `404 Not Found` dados não encontrado

```json
{
    "data": {},
    "message": "data not found"
}
```


### Retornar um aluno específico

`GET /api/student/<student_id>`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": {
        "course": "Psicologia",
        "cpf": "841.817.060-36",
        "created_on": "2021-01-29T19:26:43.551458",
        "email": "jsnow@gmail.com",
        "name": "Jon Snow",
        "phone": "(69) 99791-4811",
        "student_id": 1
    },
    "message": "successfully fetched"
}

```
- `404 Not Found` aluno não encontrado

```json
{
    "data": {},
    "message": "student not found"
}
```


### Registrando novo aluno

**Request**

`POST /api/student`

**Argumentos**

- `"name":string` -> nome do aluno 
- `"cpf":string` -> cpf do aluno
- `"course":string` -> curso do aluno
- `"email":string` -> email do aluno
- `"phone":string` -> telefone do aluno

**Response**

- `201 Created` ao ter sucesso

```json
{
    "data": {
        "course": "Pedagogia",
        "cpf": "084.596.719-33",
        "created_on": "2021-01-29T19:26:43.551458",
        "email": "cerseilan@gmail.com",
        "name": "Cersei Lannister",
        "phone": "(84) 98129-7235",
        "student_id": 3
    },
    "message": "seccessfully registered"
}
```

- `200 OK` erro com o cpf existente

```json
{
    "data": {},
    "message": "student already exists"
}
```

- `200 OK` erro com a quantidade máxima de alunos

```json
{
    "data": {},
    "message": "student limit exceeded"
}
```

- `500 Internal error` erro com o servidor ou sistema

```json
{
    "data": {},
    "message": "server error"
}
```


### Atualizando os dados do aluno

**Request**

`PUT /api/student/<student_id>`

**Argumentos**

- `"name":string`
- `"cpf":string`
- `"course":string`
- `"email":string`
- `"phone":string`

**Response**

- `201 Created` ao ter sucesso

```json
{
    "data": {
        "course": "Pedagogia",
        "cpf": "084.596.719-33",
        "created_on": "2021-01-29T19:26:43.551458",
        "email": "cerseilan@gmail.com",
        "name": "Cersei Lannister",
        "phone": "(84) 98129-7235",
        "student_id": 3
    },
    "message": "successfully updated"
}
```

- `404 Not Found` aluno não encontrado

```json
{
    "data": {},
    "message": "student not found"
}
```

- `500 Internal error` erro com servidor ou sistema

```json
{
    "data": {},
    "message": "server error"
}
```


### Deletar um aluno

**Definição**

`DELETE /api/student/<student_id>`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": {
        "course": "Pedagogia",
        "cpf": "084.596.719-33",
        "created_on": "2021-01-29T19:26:43.551458",
        "email": "cerseilan@gmail.com",
        "name": "Cersei Lannister",
        "phone": "(84) 98129-7235",
        "student_id": 2
    },
    "message": "successfully deleted"
}
```

- `404 Not Found` aluno não encontrado

```json
{
    "data": {},
    "message": "student not found"
}
```

- `500 Internal error` erro com servidor ou sistema

```json
{
    "data": {},
    "message": "server error"
}
```


### Listar todas as provas cadastradas

**Request**

`GET /api/test`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": [
        {
            "created_on": "2021-01-29T20:05:45.393508",
            "description": "Aprova foi realizada sem consulta",
            "name": "Prova de Matemática",
            "teacher": "Anakin Skywalker",
            "template": [
                { "question": 1, "answer": "C", "weight": 5 },
                { "question": 2, "answer": "B", "weight": 1 },
                { "question": 3, "answer": "A", "weight": 2 },
                { "question": 4, "answer": "D", "weight": 1 },
                { "question": 5, "answer": "C", "weight": 1 }
            ],
            "test_id": 1
        },
        {
            "created_on": "2021-01-29T20:05:45.393508",
            "description": "Aprova foi realizada com consulta",
            "name": "Prova de Comunicação e Expressão",
            "teacher": "Leia Organa",
            "template": [
                { "question": 1, "answer": "D", "weight": 3 },
                { "question": 2, "answer": "A", "weight": 2 },
                { "question": 3, "answer": "C", "weight": 2 },
                { "question": 4, "answer": "D", "weight": 1 }
            ],
            "test_id": 2
        }
    ],
    "message": "successfully fetched"
}
```

- `404 Not Found` dados não encontrado

```json
{
    "data": {},
    "message": "data not found"
}
```

- `500 Internal error` erro com o servidor ou sistema

```json
{
    "data": {},
    "message": "server error"
}
```


### Retornar uma prova específica

`GET /api/test/<test_id>`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": {
        "created_on": "2021-01-29T20:05:45.393508",
        "description": "Aprova foi realizada com consulta",
        "name": "Prova de Comunicação e Expressão",
        "teacher": "Leia Organa",
        "template": [
            { "question": 1, "answer": "D", "weight": 3 },
            { "question": 2, "answer": "A", "weight": 2 },
            { "question": 3, "answer": "C", "weight": 2 },
            { "question": 4, "answer": "D", "weight": 1 }
        ],
        "test_id": 2
    },
    "message": "successfully fetched"
}
```

- `404 Not Found` prova não encontrado

```json
{
    "data": {},
    "message": "test not found"
}
```

- `500 Internal error` erro com o servidor ou sistema

```json
{
    "data": {},
    "message": "server error"
}
```


### Registrando uma nova prova

**Request**

`POST /api/test`

**Argumentos**

- `"name":string` -> nome da prova
- `"description":string` -> descrição da prova
- `"teacher":string` -> nome do professor
- `"template":array[object]` -> gabarito da prova   [{ "question": 1, "answer": "C", "weight": 5 }]

**Response**

- `201 Created` ao ter sucesso

```json
{
    "data": {
        "created_on": "2021-01-29T20:57:18.459013",
        "description": "Aprova foi realizada sem consulta",
        "name": "Prova de Matemática",
        "teacher": "Anakin Skywalker",
        "template": [
            { "question": 1, "answer": "C", "weight": 5 },
            { "question": 2, "answer": "B", "weight": 1 },
            { "question": 3, "answer": "A", "weight": 2 },
            { "question": 4, "answer": "D", "weight": 1 },
            { "question": 5, "answer": "C", "weight": 1 }
        ],
        "test_id": 3
    },
    "message": "seccessfully registered"
}
```

- `200 OK` incapaz de criar a prova

```json
{
    "data": {},
    "message": "unable to create test"
}
```

- `500 Internal error` erro com o servidor ou sistema

```json
{
    "data": {},
    "message": "server error"
}
```


### Deletar um prova

**Definição**

`DELETE /api/test/<test_id>`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": {
        "created_on": "2021-01-29T20:05:45.393508",
        "description": "Aprova foi realizada sem consulta",
        "name": "Prova de Matemática",
        "teacher": "Anakin Skywalker",
        "test_id": 1
    },
    "message": "successfully deleted"
}
```

- `404 Not Found` prova não encontrado

```json
{
    "data": {},
    "message": "test not found"
}
```

- `500 Internal error` erro com servidor ou sistema

```json
{
    "data": {},
    "message": "server error"
}
```


### Registrando as respostas de cada prova de cada aluno

**Request**

`POST /api/student_test`

**Argumentos**

- `"student_id":string` -> id do aluno
- `"test_id":string` -> id da prova 
- `"answers":array[object]` -> resposta de cada pergunta   [{ "question": 1, "answer": "A" }]

> OBS: As respostas do aluno devem seguir o padrão do gabarito da prova.

**Response**

- `201 Created` ao ter sucesso

```json
{
    "data": {
        "answers": [
            { "question": 1, "answer": "D" },
            { "question": 2, "answer": "A" },
            { "question": 3, "answer": "C" },
            { "question": 4, "answer": "A" }
        ],
        "created_on": "2021-01-29T21:11:10.706341",
        "student_id": 1,
        "student_test_id": 1,
        "test_id": 2
    },
    "message": "seccessfully registered"
}
```

- `404 Not Found` prova e aluno não encontrados

```json
{
    "data": {},
    "message": "student and test not found"
}
```

- `404 Not Found` aluno não encontrado

```json
{
    "data": {},
    "message": "student not found"
}
```

- `404 Not Found` prova não encontrada

```json
{
    "data": {},
    "message": "test not found"
}
```

- `200 OK` incapaz de criar respostas de alunos

```json
{
    "data": {},
    "message": "unable to create student responses"
}
```

- `500 Internal error` erro com o servidor ou sistema

```json
{
    "data": {},
    "message": "server error"
}
```


### Listar todas as respostas dos alunos de cada prova

**Request**

`GET /api/student_test`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": [
        {
            "answers": [
                { "answer": "D", "question": 1 },
                { "answer": "A", "question": 2 },
                { "answer": "C", "question": 3 },
                { "answer": "A", "question": 4 }
            ],
            "created_on": "2021-01-29T21:11:10.706341",
            "student_id": 1,
            "student_test_id": 1,
            "test_id": 2
        },
        {
            "answers": [
                { "answer": "B", "question": 1 },
                { "answer": "D", "question": 2 },
                { "answer": "B", "question": 3 },
                { "answer": "A", "question": 4 }
            ],
            "created_on": "2021-01-29T21:25:03.331504",
            "student_id": 2,
            "student_test_id": 2,
            "test_id": 2
        }
    ],
    "message": "successfully fetched"
}
```

- `404 Not Found` dados não encontrado

```json
{
    "data": {},
    "message": "data not found"
}
```

- `500 Internal error` erro com o servidor ou sistema

```json
{
    "data": {},
    "message": "server error"
}
```


### Listar todas as respostas de provas de um aluno específico

`GET /api/student_test/<student_id>`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": {
        "answers": [
            { "answer": "D", "question": 1 },
            { "answer": "A", "question": 2 },
            { "answer": "C", "question": 3 },
            { "answer": "A", "question": 4 }
        ],
        "created_on": "2021-01-29T21:11:10.706341",
        "student_id": 1,
        "student_test_id": 1,
        "test_id": 2
    },
    "message": "successfully fetched"
}
```

- `404 Not Found` dados não encontrado

```json
{
    "data": {},
    "message": "data not found"
}
```


### Listar a nota final de todos os alunos vinculados ao id da prova

`GET /api/final_grade_by_test/<test_id>`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": [
        {
            "final_grade": 9,
            "name": "Jon Snow",
            "status": "aprovado",
            "student_id": 1
        },
        {
            "final_grade": 6,
            "name": "Cersei Lannister",
            "status": "reprovado",
            "student_id": 2
        }
    ],
    "message": "successfully fetched"
}
```

> OBS: A nota final da prova é sempre maior que 0 e menor que 10.

- `404 Not Found` prova não encontrada

```json
{
    "data": {},
    "message": "test not found"
}
```

- `500 Internal error` erro com o servidor ou sistema

```json
{
    "data": {},
    "message": "server error"
}
```



### Listar a nota final de todas as provas vinculados ao id do aluno

`GET /api/final_grade_by_student/<student_id>`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": [
        {
            "final_grade": 9.0,
            "name": "Jon Snow",
            "status": "aprovado",
            "student_id": 1
        }
    ],
    "message": "successfully fetched"
}
```

> OBS: A nota final da prova é sempre maior que 0 e menor que 10.

- `404 Not Found` aluno não encontrado

```json
{
    "data": {},
    "message": "student not found"
}
```

- `404 Not Found` prova não encontrada 

```json
{
    "data": {},
    "message": "test not found"
}
```

- `404 Not Found` respostas do aluno não encontradas

```json
{
    "data": {},
    "message": "answers not found"
}
```

- `500 Internal error` erro com o servidor ou sistema

```json
{
    "data": {},
    "message": "server error"
}
```
