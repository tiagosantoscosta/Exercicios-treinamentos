
 function clickMenu() {  //função para quando clicar no menu hamburguer as opções aparecerem
    if (itens.style.display == 'block'){
        itens.style.display = 'none'
    } else {
        itens.style.display = 'block'
    }    
}

function mudouTamanho(){ //função para quando a tela for maior ou igual a 768px o menu voltar a aperecer
    if (window.innerWidth >= 768){
        itens.style.display = 'block'
    } else {
        itens.style.display = 'none'
    }   
}
