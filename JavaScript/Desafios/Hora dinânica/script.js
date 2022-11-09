function carregar(){

    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours() 
    var msg2 = document.getElementById('msg2')
    msg.innerHTML = `Agora são ${hora} horas.`
    

    if (hora >= 0 && hora < 12) {
        img.src = 'manha.png'
        document.body.style.background = 'rgb(237, 227, 111)'
        msg2.innerHTML += `Bom dia!`
    } else if (hora >= 12 && hora < 18){
        img.src = 'tarde.png'
        document.body.style.background = '#a75a4c'
        msg2.innerHTML += `Boa tarde!`
    }else {
        img.src = 'noite.png'
        document.body.style.background = '#303350'
        msg2.innerHTML += `Boa noite!`
    }
}