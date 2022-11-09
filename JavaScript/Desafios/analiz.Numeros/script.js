let num = document.getElementById('fnum')
let lista = document.getElementById('flista')
let res = document.getElementById('res')
let valores = []

function isNumero(n){
    if ( Number(n) >= 1 && Number(n) <= 100) {
        return true
    } else {
        return false
    }
}

function inLista(n, l){
    if ( l.indexOf(Number(n)) != -1) {
        return true
    } else {
        return false
    }
}

function adicionar(){
    if ( isNumero(num.value) && !inLista(num.value, valores)){
        valores.push(Number(num.value))
        let item = document.createElement('option')
        item.text = `Valor ${num.value} adicionado com sucesso.`
        lista.appendChild(item)
        res.innerHTML = ``
    } else {
        alert('Valor inválido ou já encontrado na lista.')
    }
    num.value = ``
    num.focus()
}

function finalizar(){
    if ( valores.length == 0){
        alert('Adicione valores antes de finalizar')
    } else {
        res.innerHTML = ``
        res.innerHTML= `Ao todo temos ${valores.length} números cadastrados <br> `
        res.innerHTML += `O maior valor encontrado foi ${Math.max.apply(null,valores)}. <br>`
        res.innerHTML += `O menor valor encontrado foi ${Math.min(...valores)}. <br>`
        let soma = 0
        
        for ( var c in valores){
            soma = soma + valores[c]
            } 
        res.innerHTML += `Somando todos os valores temos ${soma}. <br>`
        res.innerHTML += `A média de todos os valores é ${soma/valores.length.toFixed(2)}.`
    }
}