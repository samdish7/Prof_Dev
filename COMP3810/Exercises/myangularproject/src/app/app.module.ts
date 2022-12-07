import { NgModule } from '@angular/core';
//imports array
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
//delcarations array
import { AppComponent } from './app.component';
import { CounterComponent } from './counter/counter.component';
import { BookInvComponent } from './book-inv/book-inv.component';
import { PhotoGalleryComponent } from './photo-gallery/photo-gallery.component';
import { ExamplePipe } from './example.pipe';
import { BtnDirective } from './btn.directive';
import { NotDirective } from './not.directive';

@NgModule({
  declarations: [
    AppComponent,
    CounterComponent,
    BookInvComponent,
    PhotoGalleryComponent,
    ExamplePipe,
    BtnDirective,
    NotDirective,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
