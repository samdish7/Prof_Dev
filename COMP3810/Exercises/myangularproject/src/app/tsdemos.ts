let age: number = 18;
let Name: string = 'Sam D.';
console.log(age);
// Invalid!
//age = 'He';
//console.log(age);

//printPerson function
function func(a: number, n: string){
    console.log(a + " | " + n);
}

//correct
func(age, Name);

//incorrect
//func(Name, age);

function ageTest(a: number){
    if(a > 21){
        return true;
    } else {
        return false;
    }
}

console.log(ageTest(age));

class Product{
    title: string;
    price: number;
    id: number;

    constructor (public num: number){
        this.price = 5.50;
        this.title = 'Burger';
        this.id = num;
    }

}

function printDetails(p: Product){
    console.log(p.title + ' | $' + p.price + ' | ' + p.id);
    return p;
}
let p = new Product(1);
printDetails(p);
