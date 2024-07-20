use("adnanDb")

// db.createCollection("cources")

// db.cources.insertOne({
//     name:"thi si s iqbal",
//     price:0,
//     assingment:52,
//     projects:85
// })
// db.cources.insertMany( [
//     {
//       name: "John Doe",
//       price: 100,
//       assignment: 65,
//       projects: 78
//     },
//     {
//       name: "Jane Smith",
//       price: 75,
//       assignment: 58,
//       projects: 90
//     },
//     {
//       name: "Alex Johnson",
//       price: 120,
//       assignment: 72,
//       projects: 85
//     },
//     {
//       name: "Emily Brown",
//       price: 90,
//       assignment: 70,
//       projects: 80
//     },
//     {
//       name: "Michael Lee",
//       price: 110,
//       assignment: 68,
//       projects: 92
//     }])



// let a=db.cources.find({price:0})
// console.log(a)
// console.log(a.toArray())

// db.cources.updateOne({price:0},{$set:{price:1000}})
// db.cources.updateMany({price:0},{$set:{price:1000}})

db.cources.deleteMany({price:<100})

