import { Component } from '@angular/core';
import { OnInit } from '@angular/core';

@Component({
  selector: 'app-counter',
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.scss']
})
export class CounterComponent implements OnInit {
    count: number = 0;

    ngOnInit(){
        this.count = 0;
    }

    handleClick(){
        this.count += 1;
    }
}
