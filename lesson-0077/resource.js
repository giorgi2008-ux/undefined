// let

// let-ს შეულია ცვლადის შექმნა და მისი მნიშვნელობის შეცვლა
// არ შეუძლია ხელახლა შექმნა იმავე სახელით მაგ: let age = 20; let age = 21
let age = 20
age = 21
console.log(age) // print age


//  const 

// const-ს არ შეუძლია მნიშვნელობის შეცვლა და ხელახლა შექმნა
const name = "giorgi"
console.log(name)
// name = "giorgi" - შეცდომაა
//  const name = "giorgi" - შეცდომაა


// მონაცემთა ტიპები

// string - ტექსტი
let nm = "giorgi"
console.log(nm)

// number - რიცხვი
let ag = 20
console.log(ag)

// boolean - ჭეშმარიტი/მცდარი
let y = true
let x = false
console.log(y)
console.log(x)

// null - არაფერი
// აქ არაფერია სპეციალურად ჩასმული.
let car = null
console.log(car)

// undefined - არ არის განსაზღვრული
// მნიშვნელობა ჯერ საერთოდ არ აქვს მინიჭებული.
let bike
console.log(bike)

// object - ობიექტი
let obj = {
    name: "giorgi",
    age: 20,
    isStudent: true
}
console.log(obj)

// array - მასივი
let arr = [1, 2, 3, 4, 5]
console.log(arr)

// function - ფუნქცია
function greet() {
    console.log("hello")
}
greet()

// typeof - მონაცემთა ტიპის შემოწმება
console.log(typeof nm)
console.log(typeof ag)
console.log(typeof y)
console.log(typeof x)
console.log(typeof car)
console.log(typeof bike)
console.log(typeof [])
console.log(typeof function () { })