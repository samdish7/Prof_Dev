import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
//main components
import { HomeComponent } from './home/home.component';
import { CatalogComponent } from './catalog/catalog.component';

const routes: Routes = [
    {path: "", component: HomeComponent},
    {path: "catalog", component: CatalogComponent},
    {path: "account",
        loadChildren: () => import('./account/account.module').then(m => m.AccountModule)
    }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
