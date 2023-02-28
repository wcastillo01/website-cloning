const express=require("express")
const dotenv=require("dotenv")
dotenv.config()
const bodyparser = require("body-parser")
const cors = require("cors")
const app=express()
const db = require("./db.js")

app.use(bodyparser.urlencoded({
    extended:false
}))
app.use(bodyparser.json())
app.use(cors())

app.get("/:username/:password", (req, res) => {
    const username= req.params.username
    const password = req.params.password
    db.add_info(username, password)
    res.status(200).send()
})


app.listen(8080, () => {
    console.log("API running")
})

