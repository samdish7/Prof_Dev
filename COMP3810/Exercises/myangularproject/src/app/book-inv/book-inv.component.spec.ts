import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BookInvComponent } from './book-inv.component';

describe('BookInvComponent', () => {
  let component: BookInvComponent;
  let fixture: ComponentFixture<BookInvComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BookInvComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BookInvComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
