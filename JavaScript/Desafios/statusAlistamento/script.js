function somar(){
    var data = new Date()
    var ano = data.getFullYear()
    var form = document.getElementById('txtnum')
    var res = document.getElementById('res')
    res.innerHTML = ``
    if ( form.value.length == 0 || form.value.length > 4){
        alert('Dados inválidos!')
    } else {
        n = Number(form.value)
        idade = ano - n
        if ( idade > 18 ){
            var soma = idade - 18
            res.innerHTML = `Você tem ${idade} anos e passou ${soma} anos do tempo do alistamento.<br>Seu alistamento foi em ${n + 18}.`    
        } else if ( idade == 18) {
            res.innerHTML = `Você tem ${idade} anos, está na hora de se alistar`   
        } else if ( idade < 18) {
            res.innerHTML = `Você tem ${idade} anos e falta ${18-idade} para se alistar.<br>Seu alistamento será em ${n+18}.`
        }
    }   
}
  