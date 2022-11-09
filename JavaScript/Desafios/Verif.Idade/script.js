function verificar() {               //  https://www.youtube.com/watch?v=f5es-PpaUI8 
    var data = new Date()
    var ano = data.getFullYear()
    var formano = document.getElementById('txtano')
    var res = document.getElementById('res')
    if ( formano.value.length == 0 || formano.value > ano) {
        alert('ERRO! Verifique os dados e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - (formano.value)
        var genero = ``
        var img = document.createElement('img')
        img.setAttribute('id','foto')
        
        if  (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 2) {
                //bebe
                img.setAttribute('src', 'imagem/bebe.png')
            } else if (idade > 2 && idade < 10) {
                // criança
                img.setAttribute('src', 'imagem/homemcriança.png')
            } else if (idade >= 10 && idade < 21) {
                // jovem
                img.setAttribute('src', 'imagem/homemjovem.png')
            } else if (idade >= 21 && idade < 50) {
                //adulto
                img.setAttribute('src', 'imagem/homem30anos.jpg')
            } else {
                // idoso
                img.setAttribute('src', 'imagem/homemvelho.png')
            }
        } else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade <= 2 ){
                //bebe
                img.setAttribute('src', 'imagem/bebe.png')
            } else if (idade > 2 && idade < 10){
                // criança
                img.setAttribute('src', 'imagem/mulhercriança.png')
            } else if (idade >= 10 && idade < 21) {
                // jovem
                img.setAttribute('src', 'imagem/mulherjovem.png')
            } else if (idade >= 21 && idade < 50) {
                //adulto
                img.setAttribute('src', 'imagem/mulher30anos.png')
            } else {
                // idoso
                img.setAttribute('src', 'imagem/mulhervelha.png')
            }
        }
        res.innerHTML = `Detectamos ${genero} com ${idade} anos`
        res.appendChild(img)    

        }
    }
