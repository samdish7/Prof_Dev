import { Component, OnInit, Pipe, PipeTransform } from '@angular/core';
import { Publication } from '../publication';

@Component({
  selector: 'app-book-inv',
  templateUrl: './book-inv.component.html',
  styleUrls: ['./book-inv.component.scss']
})
export class BookInvComponent implements OnInit{
    
    inv: Publication[] = [
    {   
        id: 1234,
        year: 2012,
        author: "Bob Vance",
        topic: "Hit All Angles with Angular",
        price: 900.00,
        feature: false,
        photos: ["/assets/r1.jpg", "/assets/r2.jpg"]
    },
    {   
        id: 1235,
        year: 2000,
        author: "Bob Ross",
        topic: "Hit All Angels with Angular",
        price: 900.12,
        feature: false,
        photos: ["/assets/ang2.jpg", "/assets/ang1.png"]
    },
    {   
        id: 1236,
        year: 2015,
        author: "Bob Vince",
        topic: "Hit All Memory Leaks with Angular",
        price: 900.69,
        feature: true,
        photos: ["/assets/ang3.jpg", "/assets/ts1.jpg", "/assets/ts3.png"]
    },
    ]
    ngOnInit(){};
    

}
