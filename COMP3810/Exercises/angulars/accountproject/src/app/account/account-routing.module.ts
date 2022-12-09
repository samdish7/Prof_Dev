//angular imports
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
//sub components
import { AccountHomeComponent } from './account-home/account-home.component';
import { OrderHistoryComponent } from './order-history/order-history.component';
import { AddressBookComponent } from './address-book/address-book.component';

const routes: Routes = [
    {path: "", component: AccountHomeComponent},
    {path: "orders", component: OrderHistoryComponent},
    {path: "book", component: AddressBookComponent},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AccountRoutingModule { }
