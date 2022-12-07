import { Directive, ElementRef, Renderer2, HostListener } from '@angular/core';

@Directive({
  selector: '[appBtn]'
})
export class BtnDirective {
    setFontColor(color: string){
        this.renderer.setStyle(
            this.elementRef.nativeElement, 'color', color
        )
    }

    
    constructor(private elementRef: ElementRef, private renderer: Renderer2) { 
        this.setFontColor('red');
    }
    
    @HostListener('mouseenter') OnMouseEnter(){
        this.setFontColor('blue')
    }

}
