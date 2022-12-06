console.log("called");
export class Publication{
    id: number; year: number; price: number;
    photos: string[];
    author: string; topic: string;
    feature: boolean;

    constructor(i: number, y: number, p: number, ph: string[], a: string, t: string, f: boolean){
        this.id = i; this.year = y; this.price = p; this.photos = ph; this.author = a; this.topic = t; this.feature = f;
    }
}
