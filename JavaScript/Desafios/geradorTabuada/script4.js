function tabuada(){
    let num = document.getElementById('txtnum')
    let tab = document.getElementById('selectab')
    if (num.value.length == 0){
        alert('ERRO! Por favor, digite um número')

    } else {
        let n = Number(num.value)
        let c = 1
        tab.innerHTML = `` //serve pra o campo sempre começar vazio
        for ( c ; c<=10; c++ ){
            let item = document.createElement('option') // serve para criar um elemento option na tag item
            item.text = `${n} x ${c} = ${n*c}` // serve pra criar um texto no campo text de item
            tab.appendChild(item) // serve para adicionar item no select
        }
        // while ( c <= 10 ){
        //     let item = document.createElement('option')      (USANDO WHILE)
        //     item.text = `${n} x ${c} = ${n*c}`
        //     tab.appendChild(item)
        //     c++
            
        }
    }
    

    



