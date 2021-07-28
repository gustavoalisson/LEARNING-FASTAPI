async function carregarAnimais(){
    const response = await axios.get('http://127.0.0.1:8000/animais') 
    const animais = response.data
    const lista = document.getElementById('lista-animais')
    console.log(animais)

    animais.forEach(animal => {
        const item = document.createElement('li')
        item.innerText = animal.nome
        
        lista.appendChild(item)           
    });
}

function manipularForm(){
    const form_animal = document.getElementById('form-animal')
    const input_name = document.getElementById('nome')
    const input_idade = document.getElementById('idade')
    const input_sexo = document.getElementById('sexo')
    const input_cor = document.getElementById('cor')

    form_animal.onsubmit = async (event) =>{
        event.preventDefault()
        const nome_animal = input_name.value
        const idade_animal = input_idade.value
        const sexo_animal = input_sexo.value
        const cor_animal = input_cor.value

        await axios.post('http://127.0.0.1:8000/animais', {
            nome: nome_animal,
            idade: idade_animal,
            sexo: sexo_animal,
            cor: cor_animal
        }) 
        alert('Animal cadastrado com sucesso')
    }
}

function app(){
    console.log('App iniciada...')
    carregarAnimais()
    manipularForm()
}

app()