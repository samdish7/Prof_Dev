import { Component, EventEmitter, Input, Output } from '@angular/core';
@Component({
  selector: 'app-photo-gallery',
  templateUrl: './photo-gallery.component.html',
  styleUrls: ['./photo-gallery.component.scss']
})
export class PhotoGalleryComponent {
    currIndex: number;
    @Input("photos")
    imageList: string[] = [];
    
    @Output("on-navigate")
    emitter = new EventEmitter;
    
    constructor(){
        this.currIndex = 0;
    }
    moveNext(){
        console.log("Next " + this.imageList.length);
        if (this.currIndex < this.imageList.length - 1) {
            this.currIndex += 1;
            //Raise event with index as payload
            this.emitter.emit(this.currIndex);
        }
    }

    movePrevious(){
        console.log("Prev " + this.imageList.length);
        if (this.currIndex > 0) {
            this.currIndex -= 1;
            //Raise event with index as payload
            this.emitter.emit(this.currIndex);
        }
    }
}
