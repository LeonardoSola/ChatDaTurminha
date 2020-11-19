var express = require('express')
var bodyParser = require('body-parser')
var port = 80

var app = express()

app.use(bodyParser.json())
app.use(function (req, res, next) {
  next()
})

historico = {0: {'user': 'Server', 'message': "Server iniciado com sucesso"}}

addn=1
app.get('/', (req, res) => {
  res.send(historico)
})

app.post('/', (req, res) => {
  console.log(req.body) // populated!
  req.body.message = req.body.message.trim()
  if (req.body.user.length > 10 || req.body.user.length < 3 ){
    res.send('Nome de usuario muito grande ou muito pequeno!')
    return
  }
  if (req.body.message.length < 1){
    res.send('Mensagem muito curta!')
    return
  }
  historico[addn] = req.body
  addn++
  console.log(tamanho(historico))
    if(tamanho(historico)>21){
      j=0
      for(x in historico){
        if (j == 0){
            delete historico[x]
            j++
          }
        }
      }
  res.send('Mensagem enviada!')
})


app.listen(port, () => {
  console.log(`Pronto! http://localhost:${port}`)
})

function tamanho(obj){
  res = 0
  for(x in obj){
    res++
  }
  return res
}